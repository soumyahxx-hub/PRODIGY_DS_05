import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "US_Accidents_sample.csv")
OUTDIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "figures")
os.makedirs(OUTDIR, exist_ok=True)

print("Loading:", DATA)
df = pd.read_csv(DATA, parse_dates=['Start_Time'], low_memory=False)

# Weather impact (top 10)
plt.figure(figsize=(10,5))
df['Weather_Condition'].value_counts().head(10).plot(kind='bar')
plt.title("Top 10 Weather Conditions in Accidents")
plt.xlabel("Weather Condition")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "weather_conditions_sample.png"))
plt.close()

# Road surface condition
if 'Amenity' in df.columns:
    pass  # skip if not present

if 'Side' in df.columns:
    pass

# Visibility distribution
if 'Visibility(mi)' in df.columns:
    plt.figure(figsize=(10,4))
    sns.histplot(df['Visibility(mi)'], bins=30, kde=True)
    plt.title("Visibility Distribution during Accidents")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "visibility_distribution_sample.png"))
    plt.close()

print("Saved weather/road charts to:", OUTDIR)
