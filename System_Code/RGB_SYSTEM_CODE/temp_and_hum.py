import board
import adafruit_sht4x

# Initialize I2C and sensor
i2c = board.I2C()
sensor = adafruit_sht4x.SHT4x(i2c)

def read_temp_and_humidity():
    temperature, humidity = sensor.measurements
    return temperature, humidity
