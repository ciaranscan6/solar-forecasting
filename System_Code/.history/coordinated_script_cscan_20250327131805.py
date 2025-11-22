import csv
import board
import adafruit_bh1750

import os
import time
from datetime import datetime

# Initialize I2C
i2c = board.I2C()

# Initialize BH1750 sensor
light_sensor = adafruit_bh1750.BH1750(i2c)

# Set the main directory for the project --------------(change this to the correct path like storage device maybe)------------------
base_dir = "/home/cscan/Desktop/Project/CoordinatedScript"

# Create a directory to save images photos_dir is the path for the images
photos_dir = os.path.join(base_dir, "photos_nir")
os.makedirs(photos_dir, exist_ok=True)

# Set the csv file to save the data
csv_file = os.path.join(base_dir, "data.csv")

# function to read lux values from BH1750 sensor
def read_lux(light_sensor):
    return light_sensor.lux

# function to compute solar irradiance from lux values
def computeSolarIrradiance(lux):
    # Solar Irradiance (W/m^2) = 1/120 * Lux (solarIrradianceConversionGuide)
    return (1/120) * lux

def capture_normal_image(image_filename):
    filename = os.path.join(photos_dir, image_filename)
    os.system(f"libcamera-jpeg -o {filename}")

def capture_night_image(image_filename):
    filename = os.path.join(photos_dir, image_filename)
    os.system(f"libcamera-still --shutter 6000000 --gain 32 --denoise cdn_off -o {filename}")


def write_to_csv(timestamp, lux, solar_irradiance, image_filename):
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, lux, solar_irradiance, image_filename])
    print(f"Logged: {timestamp}, Lux: {lux}, Solar Irradiance: {solar_irradiance}, Image: {image_filename}")

def main():

    while True:
        # Get the current time
        now = datetime.now()
        
        # Only take a photo and read from the lux sensor if it's the start of a new minute
        if now.second == 0:
            # Generate a timestamped row for the csv file
            timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

            # Read Lux values from BH1750 sensor
            lux = read_lux(light_sensor)

            # Compute Solar Irradiance from Lux values
            solar_irradiance = computeSolarIrradiance(lux)

            # Generate image name
            image_filename = f"{timestamp}_nir.jpg"

            # Generate an image
            if lux < 10:
                capture_night_image(image_filename)
            else:
                capture_normal_image(image_filename)

            # Write the values to a csv file
            write_to_csv(timestamp, lux, solar_irradiance, f"/photos_nir/{image_filename}")

            # Wait at least 1 second before checking again
            time.sleep(1)

        else:
            time.sleep(0.5)  # Sleep to avoid high CPU usage

if __name__ == "__main__":
    main()
