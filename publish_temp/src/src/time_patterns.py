import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "US_Accidents_sample.csv")
OUTDIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "figures")
os.makedirs(OUTDIR, exist_ok=True)

df = pd.read_csv(DATA, parse_dates=['Start_Time'])

df['hour'] = df['Start_Time'].dt.hour
df['day'] = df['Start_Time'].dt.day_name()

# Heatmap: Hour vs Day
pivot = df.pivot_table(index='day', columns='hour', aggfunc='size', fill_value=0)

plt.figure(figsize=(14,6))
sns.heatmap(pivot, cmap="viridis")
plt.title("Accident Frequency Heatmap (Day vs Hour)")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "time_heatmap_sample.png"))
plt.close()

print("Saved time heatmap.")
