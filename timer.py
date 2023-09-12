import pandas as pd

# Read the session_info.csv file
session_info_file = 'session_info.csv'
session_info_df = pd.read_csv(session_info_file)

# Read the new_data_file.csv file
new_data_file = 'new_data_file.csv'
new_data_df = pd.read_csv(new_data_file)

print(new_data_df['profile_id'].dtype)
print(session_info_df['average_timestamp'].dtype)

new_data_df['timestamp'] = pd.to_datetime(new_data_df['timestamp'])

# Convert the 'average_timestamp' column in session_info_df to datetime
session_info_df['average_timestamp'] = pd.to_datetime(session_info_df['average_timestamp'])


# Initialize an empty list to store the averaged values
averaged_values = []

# Iterate through each session in session_info_df
for index, session in session_info_df.iterrows():
    # Filter rows in new_data_df based on the session's profile_id and timestamp
    mask = (new_data_df['profile_id'] == session['profile_id']) & (new_data_df['timestamp'] >= session['average_timestamp'])
    session_data = new_data_df[mask]
    
    # Resample the session_data at 15-minute intervals and calculate averages
    session_data.set_index('timestamp', inplace=True)
    session_data_15min = session_data.resample('15T').mean()
    
    # Fill missing values with NaN if necessary
    session_data_15min.fillna(0, inplace=True)
    
    # Add the 'profile_id' column to session_data_15min
    session_data_15min['profile_id'] = session['profile_id']
    
    # Rename columns to include 'average' prefix
    session_data_15min = session_data_15min.rename(columns={
        'coolant': 'average_coolant',
        'stator_winding': 'average_stator_winding',
        'stator_tooth': 'average_stator_tooth',
        'torque': 'average_torque',
        'stator_yoke': 'average_stator_yoke'
    })
    
    # Append the resulting session_data_15min to the list of averaged values
    averaged_values.append(session_data_15min)

# Concatenate all the session data with 15-minute intervals
averaged_df = pd.concat(averaged_values)

# Reset the index
averaged_df.reset_index(inplace=True)

# Save the result to a new CSV file
averaged_df.to_csv('averaged_data_15min_intervals.csv', index=False)