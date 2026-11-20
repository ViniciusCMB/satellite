/**
 * @file FilesystemModule.cpp
 * @brief Filesystem management with SD card primary, LittleFS fallback
 *
 * Implements the exact SD-to-LittleFS fallback pattern from sensor_logging_fallback.ino
 * Smart storage strategy: SD card primary, LittleFS secondary for permanent storage
 * Persistent file management across reboots
 *
 * Desgaste de flash: o arquivo permanece ABERTO entre escritas (abre 1x no
 * begin/createFile), com flush() por linha. Abrir/fechar a cada pacote no
 * LittleFS journaliza metadados 5x mais rapido que os dados e esgota os
 * 1.4MB livres em ~1h.
 *
 * Erase de fabrica: compile com -D FS_ERASE_ON_BOOT para formatar o LittleFS
 * no boot (ex.: pio run -e helike_esp32c3 -t upload com build flag).
 *
 * @author Serra Rocketry Team — Mission #213
 * @date 2026
 */

#include "FilesystemModule.h"
#include <LittleFS.h>
#include <SPI.h>
#include <SD.h>

FilesystemModule::FilesystemModule() {
    // Constructor - no initialization needed, done in begin()
}

bool FilesystemModule::begin() {
    if (_initialized) {
        return isAvailable();
    }

    Serial.println("Initializing storage...");
    _initialized = true;

#ifndef BENCH_SKIP_SD
    // --- SD Card Primary (exact pattern from sensor_logging_fallback.ino) ---
    if (setupSD()) {
        _storage_type = STORAGE_SD;
        Serial.println("SD card available - using as primary storage");
        return true;
    }
#else
    Serial.println("[BENCH] SD skipped (BENCH_SKIP_SD)");
#endif

    // --- LittleFS Secondary (fallback from sensor_logging_fallback.ino) ---
    if (setupLittleFS()) {
        _storage_type = STORAGE_LITTLEFS;
        Serial.println("SD card unavailable - falling back to LittleFS");
        return true;
    }

    Serial.println("ERROR: No storage available!");
    _storage_type = STORAGE_NONE;
    return false;
}

String FilesystemModule::getTypeString() const {
    switch (_storage_type) {
        case STORAGE_SD:
            return "SD card (persistent file)";
        case STORAGE_LITTLEFS:
            return "LittleFS (persistent file)";
        case STORAGE_NONE:
            return "NONE";
        default:
            return "UNKNOWN";
    }
}

bool FilesystemModule::createFile(const char* path, const String& header) {
    if (!isAvailable() || _storage_type == STORAGE_NONE) {
        return false;
    }

    // Fecha handle anterior antes de trocar de arquivo/storage
    if (_log) {
        _log.close();
    }

    File file;
    if (_storage_type == STORAGE_SD) {
        file = SD.open(path, FILE_WRITE);
    } else {
        file = LittleFS.open(path, FILE_WRITE);
    }

    if (!file) {
        Serial.println("Failed to open data file.");
        return false;
    }

    file.println(header);
    file.flush();
    // Mantem aberto para escritas subsequentes (ver nota de desgaste no topo)
    _log = file;
    _log_path = path;
    return true;
}

bool FilesystemModule::appendLine(const String& packet) {
    if (!isAvailable() || _storage_type == STORAGE_NONE) {
        return false;
    }

    // Caminho rapido: arquivo ja aberto
    if (_log) {
        size_t written = _log.println(packet);
        _log.flush();
        if (written == 0) {
            // Escrita falhou (ex.: SD removido): invalida o handle para que o
            // proximo ciclo reabra e, apos SD_MAX_FAILS, degrade p/ LittleFS.
            Serial.println("[FS] ERROR: write failed - invalidating handle");
            _log = File();
            if (_storage_type == STORAGE_SD && ++_sd_fail_count >= SD_MAX_FAILS) {
                degradeToLittleFS();
            }
            return false;
        }
        _sd_fail_count = 0;
        return true;
    }

    // Fallback: reabre (ex.: depois de erro de escrita)
    File file;
    if (_storage_type == STORAGE_SD) {
        file = SD.open(_log_path.c_str(), FILE_APPEND);
    } else {
        file = LittleFS.open(_log_path.c_str(), FILE_APPEND);
    }

    if (!file) {
        // SD morreu em voo (ex: queda de alimentacao): degrada p/ LittleFS
        if (_storage_type == STORAGE_SD && ++_sd_fail_count >= SD_MAX_FAILS) {
            degradeToLittleFS();
        }
        return false;
    }

    _sd_fail_count = 0;
    _log = file;
    size_t written = _log.println(packet);
    _log.flush();
    if (written == 0) {
        _log = File();
        return false;
    }
    return true;
}

bool FilesystemModule::exists(const char* path) const {
    if (!isAvailable() || _storage_type == STORAGE_NONE) {
        return false;
    }

    if (_storage_type == STORAGE_SD) {
        return SD.exists(path);
    } else {
        return LittleFS.exists(path);
    }
}

// --- Private Implementation ---

bool FilesystemModule::setupSD() {
    Serial.println("Initializing SD...");

    // Sequencia robusta de init (spec SD): ambos CS em HIGH antes de tocar
    // o barramento, evita que o RFM95W (NSS=7) responda junto no mount
    pinMode(SD_CS_PIN, OUTPUT);
    digitalWrite(SD_CS_PIN, HIGH);
    pinMode(LORA_CS, OUTPUT);
    digitalWrite(LORA_CS, HIGH);

    // SPI manual com clock baixo: 80+ clocks de wake-up com barramento
    // ocioso (CS alto). Sem isso o cartao pode engatar deslocado e o
    // SD.begin() falha de forma intermitente ("no token received").
    // IMPORTANTE: NAO chamar spi->begin() aqui (o main ja iniciou) nem
    // SD.end() em falha — ambos desligam/reconfiguram o periferico SPI
    // e corrompem a configuracao do radio LoRa no mesmo barramento.
    SPIClass *spi = &SPI;
    SPISettings slow(400000, MSBFIRST, SPI_MODE0);
    spi->beginTransaction(slow);
    for (int i = 0; i < 20; i++) spi->transfer(0xFF);
    spi->endTransaction();
    digitalWrite(SD_CS_PIN, HIGH);

    // Tentativa 1: clock nominal. Sem retry com SD.end() — ver nota acima.
    if (!SD.begin(SD_CS_PIN, *spi, 4000000U)) {
        return false;
    }

    if (SD.cardType() == CARD_NONE) {
        return false;
    }
    Serial.printf("SD OK — type: %s  size: %llu MB\n",
        SD.cardType() == CARD_MMC ? "MMC" :
        SD.cardType() == CARD_SD  ? "SDSC" : "SDHC",
        SD.cardSize() * 512ULL / 1048576ULL);
    return true;
}

bool FilesystemModule::setupLittleFS() {
    Serial.println("SD failed. Trying LittleFS...");
#ifdef FS_ERASE_ON_BOOT
    Serial.println("[FS] FS_ERASE_ON_BOOT: formatting LittleFS...");
    if (LittleFS.format()) {
        Serial.println("[FS] LittleFS formatted.");
    } else {
        Serial.println("[FS] LittleFS format FAILED — mounting anyway.");
    }
#endif
    if (LittleFS.begin(true)) {
        Serial.printf("LittleFS OK — %u bytes free\n",
            (unsigned)(LittleFS.totalBytes() - LittleFS.usedBytes()));
        return true;
    }
    Serial.println("LittleFS mount failed.");
    return false;
}

void FilesystemModule::degradeToLittleFS() {
    Serial.println("[FS] SD failed repeatedly - switching to LittleFS");
    SD.end();
    _storage_type = STORAGE_NONE;
    if (setupLittleFS()) {
        _storage_type = STORAGE_LITTLEFS;
    }
}
