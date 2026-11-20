/**
 * @file FilesystemModule.h
 * @brief Filesystem management with SD card primary, LittleFS fallback
 *
 * Smart storage strategy: SD card primary, LittleFS secondary for permanent storage
 * Follows the exact pattern from sensor_logging_fallback.ino for consistency
 *
 * @author Serra Rocketry Team — Mission #213
 * @date 2026
 */

#ifndef FILESYSTEM_MODULE_H
#define FILESYSTEM_MODULE_H

#include <Arduino.h>
#include <FS.h>
#include "config.h"

/**
 * @enum StorageType
 * @brief Storage selection with SD primary, LittleFS fallback
 */
enum StorageType { STORAGE_NONE, STORAGE_SD, STORAGE_LITTLEFS };

/**
 * @class FilesystemModule
 * @brief Handles filesystem operations with smart fallback strategy
 *
 * Implements the exact SD-to-LittleFS fallback pattern from sensor_logging_fallback.ino
 * allowing smooth transition between storage media and maintaining persistent file naming
 */
class FilesystemModule {
public:
    FilesystemModule();

    /**
     * @brief Initialize storage with SD primary, LittleFS fallback
     * @return true if either storage type initialized successfully
     */
    bool begin();

    /**
     * @brief Check if storage is available
     * @return true if any storage type is active
     */
    bool isAvailable() const { return _storage_type != STORAGE_NONE; }

    /**
     * @brief Get human-readable storage type string
     * @return String describing current storage type
     */
    String getTypeString() const;

    /**
     * @brief Create or truncate a file for writing
     * @param path File path within the active filesystem
     * @param header Initial content/header for the file
     * @return true if file created successfully
     */
    bool createFile(const char* path, const String& header);

    /**
     * @brief Append data to an existing file
     * @param path File path within the active filesystem
     * @return true if data appended successfully
     */
    bool appendLine(const String& packet);

    /**
     * @brief Check if a file exists
     * @param path File path to check
     * @return true if file exists in current storage
     */
    bool exists(const char* path) const;

    /**
     * @brief Get current storage type
     * @return Current active storage type
     */
    StorageType getStorageType() const { return _storage_type; }

private:
    StorageType _storage_type = STORAGE_NONE;  // SD primary, LittleFS secondary
    bool        _initialized = false;
    uint8_t     _sd_fail_count = 0;            // falhas consecutivas de escrita no SD
    File        _log;                          // arquivo de telemetria mantido aberto
    String      _log_path = "/telemetry.csv";

    // Numero de falhas seguidas de appendLine() antes de degradar p/ LittleFS
    static const uint8_t SD_MAX_FAILS = 5;

    // SD card Chip Select (GPIO10 per schematic, definido em config.h)
    bool setupSD();

    // LittleFS-related
    bool setupLittleFS();

    // Degrada o armazenamento de SD para LittleFS apos falhas consecutivas
    void degradeToLittleFS();
};

#endif // FILESYSTEM_MODULE_H