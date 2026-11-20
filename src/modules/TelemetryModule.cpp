/**
 * @file TelemetryModule.cpp
 * @brief Telemetry module implementation
 */

#include "TelemetryModule.h"

TelemetryModule::TelemetryModule() : _packetCount(0) {
}

bool TelemetryModule::begin() {
    return _lora.begin();
}

void TelemetryModule::collectData(BME280Sensor &bme, ICM20602Sensor &icm, GPSSensor &gps, SensorData &data) {
    data.millis_ts = millis();

    // BME280
    if (bme.isReady()) {
        data.temperatura = bme.getTemperature();
        data.pressao = bme.getPressure();
        data.umidade = bme.getHumidity();
        data.altura = bme.getAltitude();
    } else {
        data.temperatura = NAN;
        data.pressao = NAN;
        data.umidade = NAN;
        data.altura = NAN;
    }

    // ICM-20602
    if (icm.isReady()) {
        data.ax = icm.getAx();
        data.ay = icm.getAy();
        data.az = icm.getAz();
        data.gx = icm.getGx();
        data.gy = icm.getGy();
        data.gz = icm.getGz();
    } else {
        data.ax = NAN;
        data.ay = NAN;
        data.az = NAN;
        data.gx = NAN;
        data.gy = NAN;
        data.gz = NAN;
    }

    // GPS
    if (gps.isValid()) {
        data.lat = gps.getLatitude();
        data.lon = gps.getLongitude();
        data.altura_gps = gps.getAltitude();
        data.satellites = (uint8_t)gps.getSatellites();
    } else {
        data.lat = NAN;
        data.lon = NAN;
        data.altura_gps = NAN;
        data.satellites = 0;
    }
}

void TelemetryModule::formatPacket(const SensorData &data, char *packet, size_t packetSize) {
    // 18 fields + '#' terminator — no time/date (receiver fills with local GPS)
    // TEAM_ID,millis,count,altp,temp,umi,p,gp,gr,gy,ap,ar,ay,alt,lat,lon,sat,rssi
    //
    // Mapping:
    //   altp = barometric altitude (m)
    //   temp = temperature (C)
    //   umi  = humidity (%)
    //   p    = pressure (hPa)
    //   gp   = gyroscope X (rad/s)
    //   gr   = gyroscope Y (rad/s)
    //   gy   = gyroscope Z (rad/s)
    //   ap   = accelerometer X (m/s2)
    //   ar   = accelerometer Y (m/s2)
    //   ay   = accelerometer Z (m/s2)
    //   alt  = GPS altitude (m)
    //   lat  = latitude (degrees)
    //   lon  = longitude (degrees)
    //   sat  = number of GPS satellites

    //   rssi = placeholder (-1, receiver fills this)

    _packetCount++;

    float pressao_hpa = isnan(data.pressao) ? NAN : data.pressao / 100.0f;

    snprintf(packet, packetSize,
             "%s,%lu,%lu,"                 // TEAM_ID already contains leading '#'
             "%.2f,%.2f,%.2f,%.2f,"
             "%.2f,%.2f,%.2f,"
             "%.2f,%.2f,%.2f,"
             "%.2f,%.6f,%.6f,%u,"
             "%d#",                         // trailing '#' = end-of-packet marker
             TEAM_ID, data.millis_ts, _packetCount,
              data.altura, data.temperatura, data.umidade, pressao_hpa,
              data.gx, data.gy, data.gz,
              data.ax, data.ay, data.az,
              data.altura_gps, data.lat, data.lon, data.satellites,
              -1);    // rssi placeholder
}

bool TelemetryModule::send(const String &packet) {
    Serial.println(packet);

    if (_lora.isReady()) {
        if (!_lora.send(packet)) {
            Serial.println(F("[LORA] TX fail"));
            return false;
        }
    } else {
        return false;
    }

    return true;
}
