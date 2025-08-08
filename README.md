# 24S2_nyc_transport_demand_weather

This repository analyzes the relationship between weather conditions and transportation demand in New York City, covering taxi and Citi Bike usage. The project includes data processing scripts, Jupyter notebooks for EDA, feature engineering, modeling, and visualization outputs.

## Repository Structure
```text
.
├── notebooks/                     # Jupyter notebooks for analysis and modeling
│   ├── EDA&data_Engineering.ipynb  # Exploratory data analysis and feature engineering
│   ├── modelling.ipynb             # Model training and evaluation
│   └── pre-processing.ipynb        # Data cleaning and preprocessing
│
├── plot/                           # Visualization outputs (figures, maps, plots)
│
├── report/                         # Project reports and documentation
│
├── scripts/                        # Python scripts for automation and data tasks
│   ├── __init__.py
│   └── download_data.py            # Script to download raw datasets
│
├── requirements.txt                # Python dependencies
└── MAST30034_Project_1_Muhan Chu.pdf  # Full project report
```

> **Note:** The `data/` directory is excluded from version control to keep raw and intermediate datasets private and reduce repository size.

## Objective
Investigate how weather patterns influence NYC transportation demand and build predictive models to forecast hourly demand.

## Data Sources (not included in repo)
- NYC TLC trip records (Yellow/Green Taxi)
- Citi Bike system data
- Weather data from Visual Crossing

## Methods
- Data preprocessing: cleaning, merging datasets, handling missing values
- Feature engineering: time-based features, weather conditions encoding
- Modeling:
  - Linear Regression
  - Random Forest Regression
- Visualization: spatial and temporal demand patterns

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/24S2_nyc_transport_demand_weather.git
   cd 24S2_nyc_transport_demand_weather
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download the datasets (will create the `data/` folder locally, not tracked by Git):
   ```bash
   python scripts/download_data.py
   ```
4. Run scripts or notebooks in sequence:
   ```bash
   jupyter lab
   ```
   - Start with `notebooks/pre-processing.ipynb` for data cleaning  
   - Continue with `notebooks/EDA&data_Engineering.ipynb` for feature engineering and EDA  
   - Finish with `notebooks/modelling.ipynb` for model training and evaluation

## Acknowledgements
Data sources: NYC TLC, Citi Bike, Visual Crossing Weather.
