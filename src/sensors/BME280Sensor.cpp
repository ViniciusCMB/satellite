/**
 * @file BME280Sensor.cpp
 * @brief BME280 sensor with BMP280/BMP585 fallback implementation
 */

#include "BME280Sensor.h"

BME280Sensor::BME280Sensor(float seaLevelPressure)
    : _seaLevelPressure(seaLevelPressure), _useBME(false), _useBMP585(false),
      _ready(false), _hasNewData(false) {
}

bool BME280Sensor::begin(TwoWire &wire, uint8_t addr) {
    // Try BME280 first (with humidity)
    if (_bme.begin(addr, &wire)) {
        _useBME = true;
        _useBMP585 = false;
        _ready = true;
        _hasNewData = true;
        return true;
    }

    // Fallback to BMP585 (0x46/0x47, separate address space from BMP280)
    // NOTE: Adafruit BMP5xx readPressure() returns hPa directly — getPressure()
    // callers expect Pa, so multiply by 100 here to keep the contract.
    const uint8_t bmp5Addrs[] = {0x46, 0x47};
    for (uint8_t a : bmp5Addrs) {
        if (_bmp585.begin(a, &wire)) {
            _bmp585.setTemperatureOversampling(BMP5XX_OVERSAMPLING_8X);
            _bmp585.setPressureOversampling(BMP5XX_OVERSAMPLING_16X);
            _bmp585.setIIRFilterCoeff(BMP5XX_IIR_FILTER_COEFF_3);
            _bmp585.setOutputDataRate(BMP5XX_ODR_10_HZ);
            _bmp585.setPowerMode(BMP5XX_POWERMODE_NORMAL);
            _useBME = false;
            _useBMP585 = true;
            _ready = true;
            _hasNewData = true;
            return true;
        }
    }

    // Fallback to BMP280 (no humidity) — uses default Wire internally
    if (_bmp.begin(addr)) {
        _bmp.setSampling(Adafruit_BMP280::MODE_NORMAL,
                         Adafruit_BMP280::SAMPLING_X2,
                         Adafruit_BMP280::SAMPLING_X16,
                         Adafruit_BMP280::FILTER_X16,
                         Adafruit_BMP280::STANDBY_MS_500);
        _useBME = false;
        _useBMP585 = false;
        _ready = true;
        _hasNewData = true;
        return true;
    }

    return false;
}

float BME280Sensor::getTemperature() {
    if (!_ready) return NAN;
    if (_useBME)    return _bme.readTemperature();
    if (_useBMP585) return _bmp585.readTemperature();
    return _bmp.readTemperature();
}

float BME280Sensor::getPressure() {
    if (!_ready) return NAN;
    // Contract: Pa. BMP5xx lib returns hPa — convert back.
    if (_useBMP585) return _bmp585.readPressure() * 100.0f;
    return _useBME ? _bme.readPressure() : _bmp.readPressure();
}

float BME280Sensor::getHumidity() {
    if (!_ready) return NAN;
    if (_useBME) return _bme.readHumidity();
    return NAN;  // BMP280/BMP585 have no humidity sensor
}

float BME280Sensor::getAltitude() {
    if (!_ready) return NAN;
    if (_useBMP585) return _bmp585.readAltitude(_seaLevelPressure);
    return _useBME ? _bme.readAltitude(_seaLevelPressure)
                   : _bmp.readAltitude(_seaLevelPressure);
}

void BME280Sensor::setSeaLevelPressure(float pressure) {
    _seaLevelPressure = pressure;
}

float BME280Sensor::getSeaLevelPressure() {
    return _seaLevelPressure;
}
