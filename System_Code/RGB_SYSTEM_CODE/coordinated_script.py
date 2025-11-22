import csv
import os
import time
from datetime import datetime
from temp_and_hum import read_temp_and_humidity
from rgb_camera import capture_image

#check if the external storage is mounted
if not os.path.ismount("/media/cptsc/ExtremeSSD"):
    raise RuntimeError("SSD not mounted! Check your USB connection.")


# Set the main directory for the project --------------(change this to the correct path like storage device maybe)------------------
base_dir = "/media/cptsc/ExtremeSSD/Project"

# Create a directory to save images photos_dir is the path for the images
photos_dir = os.path.join(base_dir, "photos_rgb")
os.makedirs(photos_dir, exist_ok=True)

# Set the csv file to save the data
csv_file = os.path.join(base_dir, "data.csv")

def write_to_csv(timestamp, temp, humidity, image_filename):
    with open(csv_file, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([timestamp, temp, humidity, image_filename])

    print(f"Logged: {timestamp}, Temperature: {temp}, Humidity: {humidity}, Image: {image_filename}", flush=True)

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

                    # Read Temperature and Humidity from sensor
                    temp, humidity = read_temp_and_humidity()

                    # Generate image name
                    image_filename = f"{timestamp}_rgb.jpg"

                    # Generate an image
                    capture_image(image_filename, photos_dir)

                    # Write the values to a csv file
                    write_to_csv(timestamp, temp, humidity, f"/photos_rgb/{image_filename}")

                    # Wait at least 1 second before checking again
                    time.sleep(1)
                except Exception as e:
                    print(f"Error during capture: {e}")

            else:
                time.sleep(0.5)  # Sleep to avoid high CPU usage

    except KeyboardInterrupt:
        print("Interrupted by user")

if __name__ == "__main__":
    main()
