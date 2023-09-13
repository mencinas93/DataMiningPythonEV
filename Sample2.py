import pandas as pd

# Load your dataset into a pandas DataFrame
df = pd.read_csv("resampled_data.csv")  # Replace with your file name

df['AvgStatorTemp'] = df[['stator_winding', 'stator_tooth', 'stator_yoke']].mean(axis=1)

df.to_csv("Final2.csv", index=False)
