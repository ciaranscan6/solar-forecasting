import csv
import smbus
import time

# I2C setup for BH1750
bus = smbus.SMBus(1)
BH1750_ADDR = 0x23

# BH1750 Commands
POWER_ON = 0x01
RESET = 0x07
ONE_TIME_HIGH_RES_MODE = 0x20

def auto_select_mtreg():
    trial_mtreg = 69
    set_sensitivity(trial_mtreg)
    trial_lux = read_lux(mtreg=trial_mtreg)

    if trial_lux < 5:
        mtreg = 150 # Higher resolution in very low light
    elif trial_lux < 500:
        mtreg = 120 # Still low light
    elif trial_lux < 20000:
        mtreg = 69 # Normal light
    else:
        mtreg = 32 # Bright sunlight

    return mtreg



def set_sensitivity(mtreg):
    bus.write_byte(BH1750_ADDR, POWER_ON) # Power on the sensor
    bus.write_byte(BH1750_ADDR, 0x40 | (mtreg >> 5)) # Set MTreg lower 3 bits
    bus.write_byte(BH1750_ADDR, 0x60 | (mtreg & 0x1F)) # Set MTreg upper 5 bits does XOR with 0x1F = 00011111
    bus.write_byte(BH1750_ADDR, RESET) # Reset the sensor

def read_lux(mtreg):
    bus.write_byte(BH1750_ADDR, ONE_TIME_HIGH_RES_MODE)
    time.sleep(0.180 * (mtreg / 69.0)) # Wait for the sensor to take a reading
    data = bus.read_i2c_block_data(BH1750_ADDR, ONE_TIME_HIGH_RES_MODE, 2)

    # amount from sensor, its 2 bytes, so combine them
    count = (data[0] << 8) | data[1]

    if count >= 65535:
        print("Sensor at max value")
    
    ratio = 1 / (1.2 * (mtreg / 69.0)) # Adjust for how much lux each count is worth, sensitive modes the count will be worth more lux
    lux = count * ratio

    return lux

# function to compute solar irradiance from lux values
def computeSolarIrradiance(lux):
    # Solar Irradiance (W/m^2) = 1/120 * Lux (solarIrradianceConversionGuide)
    return (1/120) * lux


