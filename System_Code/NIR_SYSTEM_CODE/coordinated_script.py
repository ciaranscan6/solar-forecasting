import csv
import os
import time
from datetime import datetime
import traceback
from light_sensor import auto_select_mtreg, set_sensitivity, read_lux, computeSolarIrradiance
from nir_camera import capture_normal_image, capture_sunny_image, capture_night_image


#check if the external storage is mounted
if not os.path.ismount("/media/cscan/USB_DISK"):
    raise RuntimeError("SSD not mounted! Check your USB connection.")


# Set the main directory for the project --------------(change this to the correct path like storage device maybe)------------------
base_dir = "/media/cscan/USB_DISK/Project"

# Create a directory to save images photos_dir is the path for the images
photos_dir = os.path.join(base_dir, "photos_nir")
os.makedirs(photos_dir, exist_ok=True)

# Set the csv file to save the data
csv_file = os.path.join(base_dir, "data.csv")

def write_to_csv(timestamp, lux, solar_irradiance, image_filename):
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, lux, solar_irradiance, image_filename])
    print(f"Logged: {timestamp}, Lux: {lux}, Solar Irradiance: {solar_irradiance}, Image: {image_filename}", flush=True)

def main():

    try:

        while True:
            
            # Get the current time
            now = datetime.now()
            
            # Only take a photo and read from the lux sensor if it's the start of a new minute
            if now.second == 0:

                try:
                    # Generate a timestamped row for the csv file
                    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

                    # Auto-select MTreg and mode based on light conditions
                    mtreg = auto_select_mtreg()
                    
                    # Set the sensitivity of the BH1750 sensor
                    set_sensitivity(mtreg)

                    # Read Lux values from BH1750 sensor
                    lux = read_lux(mtreg)

                    # Compute Solar Irradiance from Lux values
                    solar_irradiance = computeSolarIrradiance(lux)

                    # Generate image name
                    image_filename = f"{timestamp}_nir.jpg"

                    # Generate an image
                    if lux < 10:
                        capture_night_image(image_filename, photos_dir)
                    elif lux < 15000:
                        capture_sunny_image(image_filename, photos_dir)
                    else:
                        capture_normal_image(image_filename, photos_dir)

                    # Write the values to a csv file
                    write_to_csv(timestamp, lux, solar_irradiance, f"/photos_nir/{image_filename}")

                    # Wait at least 1 second before checking again
                    time.sleep(1)
                
                except Exception as e:
                    print(f"Error during capture: {e}")
                    traceback.print_exc()

            else:
                time.sleep(0.5)  # Sleep to avoid high CPU usage

    except KeyboardInterrupt:
        print("Interrupted by user")

if __name__ == "__main__":
    main()
