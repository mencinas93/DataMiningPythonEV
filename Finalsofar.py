import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load your dataset into a pandas DataFrame
df = pd.read_csv("averaged_data_15min_intervals.csv")  # Replace with your file name

# Select the columns you want to normalize and standardize
columns_to_normalize = ["average_stator_winding", "average_stator_tooth", "average_stator_yoke", "average_coolant"]
columns_to_standardize = ["average_torque"]

# Create a Min-Max scaler
minmax_scaler = MinMaxScaler()

# Create a StandardScaler for Z-score standardization
zscore_scaler = StandardScaler()

# Normalize the selected columns using Min-Max scaling
df[columns_to_normalize] = minmax_scaler.fit_transform(df[columns_to_normalize])

# Standardize the selected columns using Z-score standardization
df[columns_to_standardize] = zscore_scaler.fit_transform(df[columns_to_standardize])

# Save the preprocessed data to a new CSV file
df.to_csv("preprocessed_data.csv", index=False)