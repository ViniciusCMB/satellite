/**
 * @file config.h
 * @brief Global configuration for the Helike PocketQube satellite (#213 - LASC 2026)
 *
 * CRITICAL CONTEXT: The satellite remains COMPLETELY POWERED OFF (no energy)
 * until the rocket deploys at apogee. Upon power-on, the system is already
 * descending. There is no sleep mode, no liftoff detection.
 *
 * System objectives:
 * 1. On power-up, initialize sensors and LoRa as fast as possible
 * 2. Read sensors and transmit telemetry continuously
 * 3. No FSM, no unnecessary complexity
 *
 * @author Serra Rocketry Team — Mission #213
 * @date 2026
 */

#ifndef CONFIG_H
#define CONFIG_H

#include <Arduino.h>

//==============================================================================
// IDENTIFICATION
//==============================================================================

#define TEAM_ID             "#213"
#define MISSION_NAME        "Helike PocketQube"

//==============================================================================
// PINOUT (ESP32-C3 Super Mini)
//==============================================================================

// I2C bus
#define I2C_SDA             8
#define I2C_SCL             9

// LoRa SPI (RFM95W)
#define LORA_MOSI           6
#define LORA_MISO           5
#define LORA_SCK            4
#define LORA_CS             7
#define LORA_RST            1
#define LORA_DIO0           2

// SD Card SPI (compartilhado com LoRa)
#define SD_CS_PIN           10

// GPS UART (NEO-8M)
#define GPS_RX              20
#define GPS_TX              21

// Actuators
#define LED_PIN             3
#define BUZZER_PIN          0

//==============================================================================
// TIMING
//==============================================================================

#define SERIAL_BAUD         115200
#define GPS_BAUD            9600

// Sample interval (ms) — 200ms = 5Hz
#define SAMPLE_INTERVAL_MS  200

// Intervalo de gravacao no arquivo de backup (LittleFS/SD). LoRa transmite
// a 5Hz; o log grava a 1Hz para preservar a flash interna (ver main loop).
#define FS_LOG_INTERVAL_MS  1000

// LoRa transmission interval (ms) — same as sample rate
#define LORA_INTERVAL_MS    200

// Jitter aleatorio (±ms) aplicado ao intervalo de TX — reduz colisao com o
// foguete (#51) que transmite no mesmo canal/sync word a ~5Hz. Com ±40ms de
// jitter e pacote de ~50ms no ar, a fracao de colisoes cai proporcionalmente
// ao intervalo.
#define LORA_JITTER_MS      40

// Beep de localizacao em solo (1Hz) — desligado por padrao em voo.
// Habilite na recuperacao: -D BEEP_HEARTBEAT_ENABLED=1
#ifndef BEEP_HEARTBEAT_ENABLED
#define BEEP_HEARTBEAT_ENABLED 0
#endif
#define BEEP_HEARTBEAT_PERIOD_MS 1000

// GPS read interval (ms)
#define GPS_READ_INTERVAL_MS 1000

// Debug serial print interval (ms)
#define DEBUG_PRINT_INTERVAL_MS 2000

//==============================================================================
// LORA
//==============================================================================

#define LORA_FREQ           915E6           // Americas (Brasil)
#define LORA_SYNC_WORD      0xF3
#define LORA_TX_POWER       20              // dBm maximo
#define LORA_SPREADING      7               // SF7
#define LORA_BANDWIDTH      125E3           // 125kHz

//==============================================================================
// SENSORS
//==============================================================================

// BME280 barometric sensor
#define BME280_ADDR         0x76
#define BME280_SEALEVEL_HPA 1013.25f

// ICM-20602 IMU
#define ICM20602_ADDR       0x69
#define ACCEL_SCALE         16.0f           // ±16g
#define GYRO_SCALE           2000.0f         // ±2000°/s

// Data validation limits
#define VALID_MAX_ACCEL     (20.0f * 9.80665f)  // ±20g maximum
#define VALID_MIN_PRESSURE  30000.0f            // Pa
#define VALID_MAX_PRESSURE  120000.0f           // Pa
#define VALID_MAX_VZ        200.0f              // m/s

//==============================================================================
// WATCHDOG
//==============================================================================

#define WATCHDOG_TIMEOUT_MS 5000            // 5 seconds

//==============================================================================
// DEBUG
//==============================================================================

#define DEBUG_ENABLED      1
#define LORA_DEBUG_LOGS     0

// LittleFS: enable for flash logging (hardware test / bench)
// In real flight, disable to save power / flash wear
#define USE_LITTLEFS       1

#endif // CONFIG_H
