import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load your dataset into a pandas DataFrame
df = pd.read_csv("data_without_outliers.csv")  # Replace with your file name

# Select the columns you want to normalize and standardize
columns_to_normalize = ["stator_winding", "stator_tooth", "stator_yoke", "coolant"]
columns_to_standardize = ["torque"]

# Create a Min-Max scaler
minmax_scaler = MinMaxScaler()

# Create a StandardScaler for Z-score standardization
zscore_scaler = StandardScaler()

# Normalize the selected columns using Min-Max scaling
df[columns_to_normalize] = minmax_scaler.fit_transform(df[columns_to_normalize])

# Standardize the selected columns using Z-score standardization
df[columns_to_standardize] = zscore_scaler.fit_transform(df[columns_to_standardize])

# Save the preprocessed data to a new CSV file
df.to_csv("Normalization_preprocessed_data.csv", index=False)  