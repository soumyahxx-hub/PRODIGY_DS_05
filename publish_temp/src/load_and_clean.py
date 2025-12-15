# src/load_and_clean.py (replace your current file with this)
import pandas as pd
import glob
import os
import sys

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
DATA_DIR = os.path.abspath(DATA_DIR)

# find csv files in data folder
csv_files = glob.glob(os.path.join(DATA_DIR, "*.csv"))

if not csv_files:
    print("No CSV file found in:", DATA_DIR)
    print("Contents:", os.listdir(DATA_DIR))
    print("\nIf you downloaded the Kaggle dataset, ensure the CSV is in the 'data' folder.")
    sys.exit(1)

# if there are multiple, prefer the one that contains 'accident' or pick the first
chosen = None
for f in csv_files:
    if 'accident' in os.path.basename(f).lower():
        chosen = f
        break
if chosen is None:
    chosen = csv_files[0]

print("Using CSV file:", chosen)

# load (use low_memory=False to avoid dtype warnings)
df = pd.read_csv(chosen, low_memory=False)

# basic checks
print("Shape:", df.shape)
print("Columns:", list(df.columns)[:30])

# --- basic cleaning & features ---
# convert Start_Time if exists
if 'Start_Time' in df.columns:
    df['Start_Time'] = pd.to_datetime(df['Start_Time'], errors='coerce')
    df = df.dropna(subset=['Start_Time'])
    df['hour'] = df['Start_Time'].dt.hour
    df['dayofweek'] = df['Start_Time'].dt.day_name()
    df['month'] = df['Start_Time'].dt.month
else:
    print("Warning: 'Start_Time' column not found. Skipping time-based features.")

# ensure coordinates exist before dropping
if 'Start_Lat' in df.columns and 'Start_Lng' in df.columns:
    df = df.dropna(subset=['Start_Lat','Start_Lng'])
else:
    print("Warning: latitude/longitude columns not found. You may need to check column names.")

OUT = os.path.join(DATA_DIR, "US_Accidents_cleaned.csv")
df.to_csv(OUT, index=False)
print("Saved cleaned file to:", OUT)
