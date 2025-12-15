import pandas as pd
import glob
import os
import sys

DATA_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data"))

# try to find the CSV automatically
candidates = glob.glob(os.path.join(DATA_DIR, "*accident*.csv")) + \
             glob.glob(os.path.join(DATA_DIR, "*US_Accidents*.csv"))

if not candidates:
    print("No accident CSV found in:", DATA_DIR)
    print("Files:", os.listdir(DATA_DIR))
    sys.exit(1)

csv_path = candidates[0]
print("Using source CSV:", csv_path)

sample_out = os.path.join(DATA_DIR, "US_Accidents_sample.csv")
n = 50000  # 50k rows sample
chunksize = 200_000

collected = []
rows_collected = 0

for chunk in pd.read_csv(csv_path, chunksize=chunksize, low_memory=False):
    need = n - rows_collected
    if need <= 0:
        break

    take = min(max(1, int(len(chunk) * 0.05)), need)
    collected.append(chunk.sample(n=take, random_state=42))

    rows_collected = sum(len(c) for c in collected)
    print(f"Collected {rows_collected}/{n} rows so far...")

# combine chunks
df = pd.concat(collected, ignore_index=True)

# trim if overshoot
if len(df) > n:
    df = df.sample(n=n, random_state=42)

df.to_csv(sample_out, index=False)
print("Saved sample to:", sample_out, "rows:", len(df))

