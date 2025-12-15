Accident Analysis & Prediction Project

This repository contains a complete data analysis and modeling workflow for understanding accident patterns and identifying key factors that influence accident severity, frequency, and hotspots. The project includes data preprocessing, exploratory data analysis (EDA), visualization pipelines, predictive modeling, and automated output generation.

Key Features

Structured project with modular folders (src/, data/, notebooks/, outputs/)

Cleaned and validated accident datasets (public sample files only)

Automated scripts for generating:

Heatmaps

Hotspot maps

Time-based and weather-based accident trends

Severity and distribution plots

Reproducible EDA and modeling workflows

Machine learning components integrated for predictive tasks

Publish-ready output files generated through the publish_temp/ workflow

MIT License included for open and flexible usage

Project Structure
src/
    ├── eda_basic.py
    ├── load_and_clean.py
    ├── make_sample.py
    ├── map_hotspots_sample.py
    ├── time_patterns.py
    ├── weather_road_analysis.py
predict.py
train_tree.py
outputs/
    ├── figures/
    ├── maps/
publish_temp/ (generated during publishing)
data/ (raw data excluded via .gitignore)
notebooks/

How to Use

Clone the repository:

git clone https://github.com/soumyahxx-hub/PRODIGY_DS_05.git


Install required dependencies:

pip install -r requirements.txt


Run the preprocessing and EDA modules:

python src/load_and_clean.py
python src/eda_basic.py


Generate visual outputs:

python src/time_patterns.py
python src/map_hotspots_sample.py


Train the prediction model:

python train_tree.py

License

This project is licensed under the MIT License, allowing personal and commercial use with minimal restrictions.
