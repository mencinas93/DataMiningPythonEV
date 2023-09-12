import pandas as pd

# Replace 'your_data_file.csv' with the actual file path
file_path = 'data_without_outliers.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Calculate the timestamp column based on the sampling rate (2 Hz)
# Each row represents a data point sampled every 0.5 seconds
df['timestamp'] = pd.date_range(start='2023-09-11', periods=len(df), freq='500L')

# Select the columns you want to keep
selected_columns = ['timestamp', 'stator_winding', 'stator_yoke', 'stator_tooth', 'coolant', 'profile_id', 'torque']

# Create a new DataFrame with selected columns
selected_df = df[selected_columns]

# Save the DataFrame to a new CSV file
selected_df.to_csv('new_data_file.csv', index=False)