import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

sns.set(style="darkgrid")

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "US_Accidents_sample.csv")
OUTDIR = os.path.join(os.path.dirname(__file__), "..", "outputs", "figures")
os.makedirs(OUTDIR, exist_ok=True)

print("Loading:", DATA)
df = pd.read_csv(DATA, parse_dates=['Start_Time'], low_memory=False)
print("Rows,Cols:", df.shape)

# Extract time components
df['hour'] = df['Start_Time'].dt.hour
df['dayofweek'] = df['Start_Time'].dt.day_name()

# 1) accidents by hour
plt.figure(figsize=(10,4))
sns.countplot(x='hour', data=df, order=range(24))
plt.title("Accidents by Hour")
plt.xlabel("Hour of Day")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "accidents_by_hour_sample.png"))
plt.close()

# 2) accidents by day of week
order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
plt.figure(figsize=(9,4))
sns.countplot(x='dayofweek', data=df, order=order)
plt.title("Accidents by Day of Week")
plt.tight_layout()
plt.savefig(os.path.join(OUTDIR, "accidents_by_day_sample.png"))
plt.close()

# 3) severity distribution
if 'Severity' in df.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(x='Severity', data=df)
    plt.title("Severity Distribution")
    plt.tight_layout()
    plt.savefig(os.path.join(OUTDIR, "severity_dist_sample.png"))
    plt.close()

print("Saved figures to:", OUTDIR)
