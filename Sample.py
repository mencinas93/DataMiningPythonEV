import pandas as pd

# Read your CSV file into a DataFrame
df = pd.read_csv('dataset_with_timestamps.csv')

# Convert the 'timestamp' column to a datetime object
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set the 'timestamp' column as the index
df.set_index('timestamp', inplace=True)

# Select columns for resampling (excluding 'profile_id')
columns_to_resample = [
    'coolant',
    'stator_winding',
    'stator_tooth',
    'motor_speed',
    'pm',
    'stator_yoke',
    'ambient',
    'torque',
]

# Create a custom resampling function that retains the last 'profile_id' value
def custom_resampler(array_like):
    return array_like[-1]

# Resample the selected columns into 15-minute intervals and calculate the mean for each interval
resampled_df = df[columns_to_resample].resample('15T').mean()

# Apply the custom resampling function to the 'profile_id' column
resampled_df['profile_id'] = df['profile_id'].resample('15T').apply(custom_resampler)

# Reset the index to have the 'timestamp' as a regular column
resampled_df.reset_index(inplace=True)

# Save the resampled data to a new CSV file
resampled_df.to_csv('resampled_data.csv', index=False)