/**
 * @file LoRaModule.h
 * @brief LoRa communication module for the RFM95W radio
 *
 * SPI communication. Sends telemetry packets via LoRa radio
 * at the configured frequency (915 MHz for the Americas).
 *
 * @author Serra Rocketry Team — Mission #213
 * @date 2026
 */

#ifndef LORA_MODULE_H
#define LORA_MODULE_H

#include <Arduino.h>
#include <LoRa.h>
#include "config.h"
/**
 * @class LoRaModule
 * @brief RFM95W LoRa radio controller
 */
class LoRaModule {
public:
    LoRaModule();

    /**
     * @brief Initializes LoRa with configured pins and frequency
     * @return true if initialized successfully
     */
    bool begin();

    /**
     * @brief Sends a message via LoRa
     * @param message String to transmit
     * @return true if transmission was successful
     */
    bool send(const String &message);

    /**
     * @brief Checks if module is operational
     */
    bool isReady() const { return _ready; }

private:
    bool _ready;
    uint8_t readReg(uint8_t reg);
};

#endif // LORA_MODULE_H
