import os

def capture_image(image_filename, photos_dir):
    filename = os.path.join(photos_dir, image_filename)
    os.system(f"libcamera-jpeg -o {filename}")
