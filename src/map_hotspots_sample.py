import pandas as pd
import folium
from folium.plugins import HeatMap
import os

DATA = os.path.join(os.path.dirname(__file__), "..", "data", "US_Accidents_sample.csv")
OUTMAP = os.path.join(os.path.dirname(__file__), "..", "outputs", "maps", "accident_hotspots_sample.html")

os.makedirs(os.path.dirname(OUTMAP), exist_ok=True)

print("Loading:", DATA)
df = pd.read_csv(DATA, low_memory=False)

# Keep only valid points
df = df[['Start_Lat', 'Start_Lng']].dropna()

# Take smaller sample for map performance
small = df.sample(n=min(20000, len(df)), random_state=42)

# Create map centered at average coordinates
center = [small['Start_Lat'].mean(), small['Start_Lng'].mean()]
m = folium.Map(location=center, zoom_start=5)

# Add heatmap layer
HeatMap(list(zip(small.Start_Lat, small.Start_Lng)), radius=7).add_to(m)

m.save(OUTMAP)
print("Map saved to:", OUTMAP)
