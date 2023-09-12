import pandas as pd

# Load your dataset into a pandas DataFrame
df = pd.read_csv("preprocessed_data.csv")  # Replace with your file name

df['AvgStatorTemp'] = df[['average_stator_winding', 'average_stator_tooth', 'average_stator_yoke']].mean(axis=1)

df.to_csv("Final1.csv", index=False)
