# Final Year Project – Solar Irradiance Forecasting System

This repository contains all code, data, models, and CAD designs for a **low-cost solar irradiance forecasting system**. The system integrates environmental sensors, sky imaging (RGB and NIR), and LSTM-based forecasting models.

## Repository Structure

Each folder has a seperate README that provides more details on specific directories

- **CAD_Parts_and_Drawings/**  
  CAD models and technical drawings of the system’s enclosure.

- **Correlation_Graphs/**  
  Jupyter notebook and datasets for generating correlation graphs and heatmaps between environmental/image features and solar irradiance.

- **Data/**  
  Collected datasets including environmental sensor readings and extracted image paths (images would be too big).

- **Example_Images/**  
  Sample NIR and RGB images captured by the system.

- **Histograms/**  
  Notebook for analyzing images in NIR and RGB images as well as the images used for analysis.

- **Image_Size_Aligner/**  
  Notebook for aligning and resizing NIR images for direct comparison with rgb.

- **LSTM_Forecasting/**  
  Code and datasets for training LSTM models to forecast solar irradiance. Contains models trained both with and without camera-derived features.

- **System_Code/**  
  Data collection scripts for the NIR and RGB systems, including sensor reading scripts, bash script for starting collection, camera capture, and coordination scripts.