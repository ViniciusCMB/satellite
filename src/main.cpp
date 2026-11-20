//==============================================================================
// INCLUDES
//==============================================================================

#include <Arduino.h>
#include <Wire.h>
#include <SPI.h>
#include <esp_task_wdt.h>
#include <esp_system.h> // esp_random()

#include "config.h"
#include "calc/SensorData.h"
#include "calc/DataValidation.h"
#include "calc/VerticalVelocity.h"
#include "sensors/BME280Sensor.h"
#include "sensors/ICM20602Sensor.h"
#include "sensors/GPSSensor.h"
#include "modules/LoRaModule.h"
#include "modules/BuzzerModule.h"
#include "modules/LEDModule.h"
#include "modules/TelemetryModule.h"
#include "modules/FilesystemModule.h"

//==============================================================================
// GLOBAL OBJECTS (static, no heap allocation)
//==============================================================================

static TwoWire i2c_bus = Wire; // alias for Wire
static BME280Sensor g_bme;
static ICM20602Sensor g_icm;
static GPSSensor g_gps;
static BuzzerModule g_buzzer;
static LEDModule g_led;
static TelemetryModule g_telemetry;
static VerticalVelocity g_vz_filter(0.4f);
static DataValidation g_validator(ValidationConfig{VALID_MAX_ACCEL, VALID_MIN_PRESSURE, VALID_MAX_PRESSURE, VALID_MAX_VZ});
static FilesystemModule g_fs;

//==============================================================================
// STATE
//==============================================================================

static uint32_t g_last_sample = 0;
static uint32_t g_next_interval = SAMPLE_INTERVAL_MS;
static uint32_t g_last_debug_print = 0;
static bool g_bme_ok = false;
static bool g_icm_ok = false;
static bool g_lora_ok = false;
static uint32_t g_lora_failures = 0;
static uint32_t g_fs_failures = 0;
//==============================================================================
// SETUP
//==============================================================================

void setup() {
    // --- Serial ---
    Serial.begin(SERIAL_BAUD);
    unsigned long serialStart = millis();
    while (!Serial && (millis() - serialStart < 2000)) { ; }
    Serial.println();
    Serial.println(F("========================================"));
    Serial.print(F("  "));
    Serial.print(MISSION_NAME);
    Serial.print(F("  TEAM "));
    Serial.println(TEAM_ID);
    Serial.println(F("  LASC 2026"));
    Serial.println(F("========================================"));
    Serial.println();

    // --- Buzzer (early: beep on every boot, before any init can fail) ---
    g_buzzer.begin();
    g_buzzer.playBeep();
    Serial.println(F("[ACT] Buzzer initialized — boot beep"));

    // --- I2C (single begin — initialize global Wire for all sensors) ---
    Wire.begin(I2C_SDA, I2C_SCL);
    delay(100);
    Wire.setClock(400000); // 400kHz Fast Mode
    Serial.println(F("[I2C] Bus initialized (SDA=8, SCL=9, 400kHz)"));

    // --- LED ---
    g_led.begin();
    Serial.println(F("[ACT] LED initialized"));

    // --- BME280 (BMP280/BMP585 fallbacks inside) ---
    g_bme_ok = g_bme.begin(Wire, BME280_ADDR);
    if (g_bme_ok) {
        if (g_bme.isBMP585()) {
            Serial.println(F("[BMP] BMP585 fallback OK @ 0x46 (no humidity)"));
        } else {
            Serial.println(F("[BME] BME280 OK"));
        }
    } else {
        Serial.println(F("[BME] ERROR: no barometric sensor found!"));
    }

    // --- ICM-20602 ---
    g_icm_ok = g_icm.begin(ICM20602_ADDR, Wire);
    if (g_icm_ok) {
        Serial.println(F("[ICM] ICM-20602 OK"));
    } else {
        Serial.println(F("[ICM] ERROR: ICM-20602 not found!"));
    }

    // --- GPS ---
    g_gps.begin();
    Serial.println(F("[GPS] NEO-8M initialized (9600 baud)"));

    // --- Barramento SPI unico: inicia UMA vez, antes de SD e LoRa ---
    // Ambas as libs (SD/LoRa) chamam SPI.begin() internamente com defaults;
    // a reinicializacao dupla corrompe o estado do periferico no ESP32-C3.
    pinMode(LORA_CS, OUTPUT);  digitalWrite(LORA_CS, HIGH);
    pinMode(SD_CS_PIN, OUTPUT); digitalWrite(SD_CS_PIN, HIGH);
    SPI.begin(LORA_SCK, LORA_MISO, LORA_MOSI);

    // --- LoRa PRIMEIRO: o SD.begin/end reconfigura o periferico SPI e
    // corrompe a comunicacao com o radio se rodar antes. Com o LoRa ja
    // configurado, as transacoes SPI atomicas do SD coexistem sem conflito.
    g_lora_ok = g_telemetry.begin();
    if (g_lora_ok) {
        Serial.println(F("[LORA] RFM95W OK (915MHz)"));
    } else {
        Serial.println(F("[LORA] ERROR: RFM95W not found!"));
    }

    // --- Storage (SD primary, LittleFS fallback) ---
    if (g_fs.begin()) {
        String csv_header = "TEAM_ID,millis,count,altp,temp,umi,p,gp,gr,gy,ap,ar,ay,alt,lat,lon,sat,rssi";
        g_fs.createFile("/telemetry.csv", csv_header);
        Serial.print(F("[FS] Storage: "));
        Serial.println(g_fs.getTypeString());
    } else {
        Serial.println(F("[FS] ERROR: No storage available!"));
    }

    // --- Status summary ---
    Serial.println(F("--- Initialization Summary ---"));
    Serial.print(F("  BME280:    ")); Serial.println(g_bme_ok ? F("OK") : F("FAIL"));
    Serial.print(F("  ICM-20602: ")); Serial.println(g_icm_ok ? F("OK") : F("FAIL"));

    // --- Watchdog (ESP32-C3 TWDT) — init before beeps/blinks ---
    esp_task_wdt_init(WATCHDOG_TIMEOUT_MS * 1000, true);
    esp_task_wdt_add(NULL); // Subscribe current task

    // --- Audio/visual feedback ---
    if (g_bme_ok && g_icm_ok) {
        g_buzzer.playStartup();
        g_led.blink(3, 300);
    } else {
        g_buzzer.playError();
        g_led.blinkFast(10);
    }

    g_last_sample = millis();
    g_last_debug_print = millis();

    Serial.println(F("[SYS] Setup complete. Starting main loop..."));
    Serial.println();
}

//==============================================================================
// LOOP
//==============================================================================

void loop() {
    unsigned long now = millis();

    // --- GPS update (always, to keep parser fresh) ---
    g_gps.update();

    // --- Beep de localizacao (nao-bloqueante; ver BEEP_HEARTBEAT_ENABLED) ---
    g_buzzer.updateHeartbeat(now);

    // --- Main loop at sample interval (jitter entra no limiar) ---
    if (now - g_last_sample < g_next_interval) {
        return;
    }
    // --- Feed watchdog ---
    esp_task_wdt_reset();

    // --- Update IMU ---
    g_icm.update();

    // --- Collect data ---
    SensorData data;
    g_telemetry.collectData(g_bme, g_icm, g_gps, data);

    // --- Validate data ---
    bool valid = g_validator.isValid(data);

    // --- Calculate Vz (skip first sample — filter has no history) ---
    static bool g_first_sample = true;
    if (valid && !isnan(data.altura)) {
        if (g_first_sample) {
            g_first_sample = false;
            data.vz = NAN;
        } else {
            data.vz = g_vz_filter.update(data.altura, now);
        }
    } else {
        data.vz = NAN;
    }

    // --- Calculate gyroscope magnitude ---
    if (valid) {
        data.mag_giroscopia = sqrtf(data.gx * data.gx + data.gy * data.gy + data.gz * data.gz);
    } else {
        data.mag_giroscopia = NAN;
    }

    // --- Build CSV packet ---
    char packetBuf[160];
    g_telemetry.formatPacket(data, packetBuf, sizeof(packetBuf));
    String packet(packetBuf);

    // --- Transmit ---
    if (!g_telemetry.send(packet)) {
        g_lora_failures++;
        Serial.println(F("[LORA] ERROR: send() failed"));
    }

    // --- Log to storage (LittleFS/SD) @ 1Hz ---
    // O LoRa transmite a 5Hz (200ms); o arquivo de backup grava a 1Hz para
    // preservar a flash interna: ~70B/s vs ~350B/s. Se a flash chegar a
    // ZERO bytes livres, o log para sozinho (o LoRa segue transmittindo).
    static uint32_t s_last_log = 0;
    if (now - s_last_log >= FS_LOG_INTERVAL_MS) {
        s_last_log = now;
        if (!g_fs.appendLine(packet)) {
            g_fs_failures++;
            Serial.println(F("[FS] ERROR: appendLine() failed"));
        }
    }

    // --- Heartbeat LED ---
    g_led.toggle();

    // --- Periodic debug print ---
    if (DEBUG_ENABLED && (now - g_last_debug_print >= DEBUG_PRINT_INTERVAL_MS)) {
        g_last_debug_print = now;
        unsigned long loop_duration = now - g_last_sample;
        Serial.print(F("[DEBUG] Packet #"));
        Serial.print(g_telemetry.getPacketCount());
        Serial.print(F(" | BME:"));
        Serial.print(g_bme_ok ? F("ok") : F("--"));
        Serial.print(F(" ICM:"));
        Serial.print(g_icm_ok ? F("ok") : F("--"));
        Serial.print(F(" LoRa:"));
        Serial.print(g_lora_ok ? F("ok") : F("--"));
        Serial.print(F(" GPS sats:"));
        Serial.print(g_gps.getSatellites());
        Serial.print(F(" | Vz:"));
        Serial.print(data.vz);
        Serial.print(F(" | loop:"));
        Serial.print(loop_duration);
        Serial.print(F("ms | LoRa fails:"));
        Serial.print(g_lora_failures);
        Serial.print(F(" FS fails:"));
        Serial.println(g_fs_failures);
    }
    // --- Agenda proximo ciclo com jitter (reduz colisao com o foguete) ---
    // O jitter entra no limiar, nao no timestamp: agendar g_last_sample no
    // futuro causaria underflow em "now - g_last_sample" (unsigned) e rajadas.
    g_last_sample = now;
    g_next_interval = SAMPLE_INTERVAL_MS
        + (int32_t)(esp_random() % (2 * LORA_JITTER_MS + 1)) - LORA_JITTER_MS;
}
