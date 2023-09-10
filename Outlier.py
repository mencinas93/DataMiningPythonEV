import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load your dataset into a pandas DataFrame
df = pd.read_csv("preprocessed_data.csv")

# Select the columns you want to calculate z-scores for
columns_to_standardize = ["stator_winding", "stator_tooth", "stator_yoke", "coolant", "torque"]

# Create a StandardScaler for Z-score standardization
scaler_zscore = StandardScaler()

# Calculate z-scores for the selected columns
df[columns_to_standardize] = scaler_zscore.fit_transform(df[columns_to_standardize])


# Save the z-score standardized data to a new CSV file
df.to_csv("z_score_standardized_dataset.csv", index=False)