import os

def capture_normal_image(image_filename, photos_dir):
    filename = os.path.join(photos_dir, image_filename)
    os.system(f"libcamera-still -o {filename} --awb custom --awbgains 1.2,1.2")

def capture_sunny_image(image_filename, photos_dir):
    filename = os.path.join(photos_dir, image_filename)
    os.system(f"libcamera-still --shutter 500 --gain 1 --awb custom --awbgains 1.2,1.2 -o {filename}")


def capture_night_image(image_filename, photos_dir):
    filename = os.path.join(photos_dir, image_filename)
    os.system(f"libcamera-still --shutter 6000000 --gain 32 -o {filename}")