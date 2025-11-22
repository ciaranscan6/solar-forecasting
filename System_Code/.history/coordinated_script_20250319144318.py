import csv
import smbus2
import time

import os
import time
from datetime import datetime

# BH1750 Address
BH1750_I2C_ADDR = 0x23
# BH1750 Command
CONTINUOUS_HIGH_RES_MODE = 0x10

# Set the main directory for the project --------------(change this to the correct path like storage device maybe)------------------
base_dir = "/home/cscan/Desktop/Project/CoordinatedScript"

# Create a directory to save images photos_dir is the path for the images
photos_dir = os.path.join(base_dir, "photos")
os.makedirs(photos_dir, exist_ok=True)

# Set the csv file to save the data
csv_file = "/home/cscan/Desktop/Project/CoordinatedScript/data.csv"

# function to read lux values from BH1750 sensor
def read_lux(bus, addr=BH1750_I2C_ADDR):
    try:
        bus.write_byte(addr, CONTINUOUS_HIGH_RES_MODE)
        time.sleep(0.2) 
        
        # Read 2 bytes of data
        data = bus.read_i2c_block_data(addr, 0x00, 2)
        
        # Convert data to lux
        lux = (data[0] << 8) | data[1]

        return lux
    except Exception as e:
        print(f"Error reading BH1750: {e}")
        return None

# function to compute solar irradiance from lux values
def computeSolarIrradiance(lux):
    # Solar Irradiance (W/m^2) = 1/120 * Lux (solarIrradianceConversionGuide)
    return (1/120) * lux

def capture_image(timestamp):
    filename = os.path.join(photos_dir, f"{timestamp}.jpg")
    os.system(f"libcamera-jpeg -o {filename}")

def write_to_csv(timestamp, lux, solar_irradiance, image_filename):
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, lux, solar_irradiance, image_filename])

def main():
    bus = smbus2.SMBus(1)

    while True:
        # Get the current time
        now = datetime.now()
        
        # Only take a photo and read from the lux sensor if it's the start of a new minute
        if now.second == 0:
            # Generate a timestamped row for the csv file
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

            # Read Lux values from BH1750 sensor
            lux = read_lux(bus)

            # Compute Solar Irradiance from Lux values
            solar_irradiance = computeSolarIrradiance(lux)

            # Generate an image
            capture_image(timestamp)

            # Generate image name
            image_filename = f"{timestamp}.jpg"

            # Write the values to a csv file
            write_to_csv(timestamp, lux, solar_irradiance, image_filename)

            print(f"Logged: {timestamp}, Lux: {lux}, Solar Irradiance: {solar_irradiance}, Image: {image_filename}")

            # Wait at least 1 second before checking again
            time.sleep(1)

        else:
            time.sleep(0.5)  # Sleep to avoid high CPU usage

if __name__ == "__main__":
    main()
