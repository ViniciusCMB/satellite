// I2C scanner temporario — testa os pinos 8/9 (GPIO8 SDA / GPIO9 SCL) e os pinos alternativos 0/1.
// NAO subir para voo: sobrescreve src/main.cpp? NAO — vive em src/sensors_disabled/ (fora do build) e
// e compilado via ambiente dedicado abaixo.
#include <Arduino.h>
#include <Wire.h>

static void scan(TwoWire &bus, const char *label) {
    Serial.printf("\n=== Scanning %s ===\n", label);
    uint8_t found = 0;
    for (uint8_t addr = 1; addr < 127; addr++) {
        bus.beginTransmission(addr);
        if (bus.endTransmission() == 0) {
            Serial.printf("  Device found @ 0x%02X\n", addr);
            found++;
        }
    }
    if (found == 0) Serial.println("  No devices found.");
    Serial.printf("  Total: %u device(s)\n", found);
}

void setup() {
    Serial.begin(115200);
    delay(2000);
    Serial.println("\n[I2C-SCAN] HELIKE bus scanner");

    // Bus principal (SDA=8, SCL=9) — conforme esquematico
    Wire.begin(8, 9);
    Wire.setClock(100000);  // 100kHz: mais tolerante a fio longo/pull-up fraco
    scan(Wire, "SDA=8 SCL=9 @ 100kHz");
    Wire.setClock(400000);
    scan(Wire, "SDA=8 SCL=9 @ 400kHz");
    Wire.end();

    // Bus alternativo em GPIO0/GPIO1 (via Wire1) — testa hipotese de pinos trocados
    TwoWire *bus1 = &Wire1;
    bus1->begin(0, 1);
    bus1->setClock(100000);
    scan(*bus1, "SDA=0 SCL=1 @ 100kHz (alt)");
    bus1->end();
}

void loop() {
    delay(10000);
    Serial.println("--- rescan SDA=8 SCL=9 @ 100kHz ---");
    Wire.begin(8, 9);
    Wire.setClock(100000);
    scan(Wire, "SDA=8 SCL=9 @ 100kHz (rescan)");
    Wire.end();
}
