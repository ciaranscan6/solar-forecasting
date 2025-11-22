# System Code

This folder contains the data collection scripts for both the **NIR** and **RGB** systems used in the project.

## Structure

- **NIR_SYSTEM_CODE/**
  - `coordinated_script.py` – Main script coordinating NIR image capture and light sensor readings and logging them to external hard drive.
  - `nir_camera.py` – Handles NIR camera image capture.
  - `light_sensor.py` – Reads data from the light sensor.
  - `run_collector.sh` – Shell script to launch the data collection processes.

- **RGB_SYSTEM_CODE/**
  - `coordinated_script.py` – Main script coordinating RGB image capture and temp and humidity sensor and logging them to external hard drive.
  - `rgb_camera.py` – Handles RGB camera image capture.
  - `temp_and_hum.py` – Reads data from the temperature and humidity sensor.
  - `run_collector.sh` – Shell script to launch the data collection processes.

## Notes

- Each **coordinated script** manages synchronized data capture from sensors and cameras.
- The **run_collector.sh** script automates the start of the data collection system (both scripts in each system are identical).



## System Flow Diagrams Reminder

- **NIR System Flow:**

    <img src="Images_For_Readme/Page%201.jpg" alt="NIR Flow Diagram" width="150"/>

- **RGB System Flow:**


    <img src="Images_For_Readme/Page%202.jpg" alt="RGB Flow Diagram" width="150"/>