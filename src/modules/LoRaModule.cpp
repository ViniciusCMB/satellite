/**
 * @file LoRaModule.cpp
 * @brief RFM95W LoRa module implementation
 */

#include "LoRaModule.h"

LoRaModule::LoRaModule() : _ready(false) {
}

bool LoRaModule::begin() {
    // Compartilha a instancia SPI ja iniciada pelo main (barramento unico
    // com o SD). A lib sandeepmistry chama _spi->begin() sem argumentos,
    // o que reconfiguraria os pinos default da variante e corromperia o
    // barramento compartilhado.
    LoRa.setSPI(SPI);
    LoRa.setPins(LORA_CS, LORA_RST, LORA_DIO0);

    // Diagnostico: le RegVersion direto antes da lib tentar (5x para detectar
    // leitura instavel = mau contato no barramento SPI)
    pinMode(LORA_RST, OUTPUT); digitalWrite(LORA_RST, HIGH);
    delay(10);
    SPISettings probe(400000, MSBFIRST, SPI_MODE0);
    SPI.beginTransaction(probe);
    Serial.print(F("[LORA] Pre-begin RegVersion: "));
    for (int i = 0; i < 5; i++) {
        // CS deve ser reafirmado a cada leitura; caso contrario o chip
        // devolve registradores consecutivos (0x42..0x46), nao o RegVersion.
        digitalWrite(LORA_CS, LOW);
        SPI.transfer(0x42 & 0x7F);
        uint8_t ver = SPI.transfer(0xFF);
        digitalWrite(LORA_CS, HIGH);
        Serial.printf("0x%02X ", ver);
    }
    SPI.endTransaction();
    Serial.println(F("(esperado 0x12 sempre)"));

    if (!LoRa.begin(LORA_FREQ)) {
        return false;
    }

    // Configure LoRa parameters (functions return void, no direct check)
    LoRa.setSyncWord(LORA_SYNC_WORD);
    LoRa.setTxPower(LORA_TX_POWER);
    LoRa.setSpreadingFactor(LORA_SPREADING);
    LoRa.setSignalBandwidth(LORA_BANDWIDTH);
    LoRa.enableCrc();

    _ready = true;
    return true;
}

bool LoRaModule::send(const String &message) {
    if (!_ready) return false;

    // endPacket() retorna 1 em sucesso (lib sandeepmistry)
    LoRa.beginPacket();
    LoRa.print(message);

    bool ok = LoRa.endPacket() == 1;
    if (!ok) {
        // Diagnostico: le estado do radio direto via SPI na primeira falha
        static bool dumped = false;
        if (!dumped) {
            dumped = true;
            uint8_t ver  = readReg(0x42);  // RegVersion
            uint8_t mode = readReg(0x01);  // RegOpMode
            uint8_t irq  = readReg(0x12);  // RegIrqFlags
            uint8_t mdi  = readReg(0x1C);  // RegModemConfig3 (resposta valida = SPI vivo)
            Serial.printf("[LORA-DIAG] ver=0x%02X mode=0x%02X irq=0x%02X cfg3=0x%02X\n",
                          ver, mode, irq, mdi);
            Serial.println("[LORA-DIAG] irq 0x08=TXdone 0x40=RxDone; mode 0x83=TX");
        }
    }
    return ok;
}

uint8_t LoRaModule::readReg(uint8_t reg) {
    SPISettings probe(400000, MSBFIRST, SPI_MODE0);
    SPI.beginTransaction(probe);
    digitalWrite(LORA_CS, LOW);
    SPI.transfer(reg & 0x7F);
    uint8_t val = SPI.transfer(0xFF);
    digitalWrite(LORA_CS, HIGH);
    SPI.endTransaction();
    return val;
}
