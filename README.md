# Glucose Time Series AI Analysis

This project focuses on extracting time series properties of glucose levels using AI techniques, based on the Medtronic Artificial Pancreas system.

## 🧠 Overview

The project analyzes CGM (Continuous Glucose Monitor) and insulin pump data from the Medtronic 670G system to compute time-series metrics related to glucose levels. These metrics help assess the performance of manual vs. auto insulin delivery modes.

## 📊 Objectives

- Synchronize sensor data from CGM and insulin pump sources
- Handle missing data (NaNs) using interpolation or removal
- Segment data by day, daytime, and overnight windows
- Extract and report 18 metrics on glucose control for both manual and auto modes

## 📁 Files Included

- `main.py` – The main driver script to load, process, and analyze the data
- `CGMData.csv` – Continuous glucose sensor readings every 5 minutes
- `InsulinData.csv` – Insulin delivery events, carbohydrate intake, and auto-mode info
- `Result.csv` – 2x18 matrix of metrics for Manual and Auto mode
- `requirements.txt` – Python dependencies for the project

## 🧮 Metrics Computed (Per Mode)

For Manual and Auto Modes:

- % Time in Hyperglycemia (>180 mg/dL)
- % Time in Critical Hyperglycemia (>250 mg/dL)
- % Time in Range (70–180 mg/dL)
- % Time in Narrow Range (70–150 mg/dL)
- % Time in Hypoglycemia Level 1 (<70 mg/dL)
- % Time in Hypoglycemia Level 2 (<54 mg/dL)

Each metric is reported over:
- Daytime (6am–midnight)
- Overnight (midnight–6am)
- Full day (24 hrs)

## 📌 Technologies Used

- Python 3.10.9
- pandas, numpy, scipy
- Manual vs Auto mode detection
- Time-based segmentation
- CSV data handling

## 📄 Project Documentation

For a full explanation of the objectives, methods, and results, see the [Project Description (PDF)](./Project%20Description.pdf).

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python main.py
