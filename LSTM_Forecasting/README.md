# LSTM Forecasting

This folder contains LSTM models and datasets used for solar irradiance forecasting, with and without image-derived features.

## Structure

- **model_with_camera_features/**  
  LSTM model trained on environmental data combined with camera-derived image features.
  - `cleaned_data_ltsm.ipynb` – Prepares data and trains the model.
  - `data_with_camera_info.csv` – Full dataset with camera features.
  - `train_with_cam_info.csv` / `test_with_cam_info.csv` – Training and testing splits.

- **model_without_camera_features/**  
  LSTM model trained solely on environmental data, excluding camera features.
  - `cleaned_data_ltsm.ipynb` – Prepares data and trains the model.
  - `train.csv` / `test.csv` – Training and testing splits.

## Notes

- The **models/** folders in each section store saved models for further evaluation or deployment.
- This setup compares the forecasting performance of models **with** and **without** image features.
