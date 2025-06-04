import pandas as pd
import matplotlib.pyplot as plt

# Load the parsed CSV file
try:
    df = pd.read_csv('snort_alerts.csv')
except FileNotFoundError:
    print("File 'snort_alerts.csv' not found. Please check the file path.")
    exit()

# Ensure Priority column is numeric (in case it's treated as string)
df['Priority'] = pd.to_numeric(df['Priority'], errors='coerce')

# Drop rows where Priority could not be converted to number
df = df.dropna(subset=['Priority'])

# Count alerts by Priority
priority_counts = df['Priority'].value_counts().sort_index()

# Plot bar chart of alert counts by Priority
plt.figure(figsize=(8, 5))
plt.bar(priority_counts.index.astype(int), priority_counts.values, color='skyblue')
plt.xlabel('Priority')
plt.ylabel('Number of Alerts')
plt.title('Snort Alerts by Priority')
plt.xticks(priority_counts.index.astype(int))
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
