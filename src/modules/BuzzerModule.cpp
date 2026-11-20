/**
 * @file BuzzerModule.cpp
 * @brief Active buzzer implementation (digital on/off, no PWM needed)
 */

#include "BuzzerModule.h"

BuzzerModule::BuzzerModule() {
}

void BuzzerModule::begin() {
    pinMode(BUZZER_PIN, OUTPUT);
    digitalWrite(BUZZER_PIN, LOW);
}

void BuzzerModule::playStartup() {
    for (int i = 0; i < 3; i++) {
        digitalWrite(BUZZER_PIN, HIGH);
        delay(SHORT_MS);
        digitalWrite(BUZZER_PIN, LOW);
        delay(PAUSE_MS);
    }
}

void BuzzerModule::playError() {
    for (int i = 0; i < 5; i++) {
        digitalWrite(BUZZER_PIN, HIGH);
        delay(SHORT_MS);
        digitalWrite(BUZZER_PIN, LOW);
        delay(40);
    }
}

void BuzzerModule::playBeep() {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(SHORT_MS);
    digitalWrite(BUZZER_PIN, LOW);
    delay(PAUSE_MS);
}

void BuzzerModule::playContinuous(uint16_t duration_ms) {
    digitalWrite(BUZZER_PIN, HIGH);
    delay(duration_ms);
    digitalWrite(BUZZER_PIN, LOW);
}

void BuzzerModule::updateHeartbeat(uint32_t now_ms) {
#if BEEP_HEARTBEAT_ENABLED
    if (_heartbeat_on) {
        if (now_ms - _heartbeat_start_ms >= SHORT_MS) {
            digitalWrite(BUZZER_PIN, LOW);
            _heartbeat_on = false;
        }
    } else if (now_ms - _heartbeat_last_ms >= BEEP_HEARTBEAT_PERIOD_MS) {
        digitalWrite(BUZZER_PIN, HIGH);
        _heartbeat_on = true;
        _heartbeat_start_ms = now_ms;
        _heartbeat_last_ms = now_ms;
    }
#else
    (void)now_ms;
#endif
}

void BuzzerModule::stop() {
    digitalWrite(BUZZER_PIN, LOW);
}
