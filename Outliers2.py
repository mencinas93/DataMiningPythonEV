import pandas as pd
from scipy import stats

# Load your dataset into a pandas DataFrame
df = pd.read_csv("preprocessed_data.csv")

# Define the columns you want to perform outlier detection on
columns_of_interest = ["stator_winding", "stator_tooth", "stator_yoke", "coolant", "torque"]

# Define the Z-score threshold for outlier detection
z_score_threshold = 3

# Calculate Z-scores for the selected columns
z_scores = stats.zscore(df[columns_of_interest])

# Create a Boolean mask for outliers
outlier_mask = (abs(z_scores) > z_score_threshold).any(axis=1)

# Remove rows containing outliers
df_no_outliers = df[~outlier_mask]

# Save the data with outliers removed to a new CSV file
df_no_outliers.to_csv("data_without_outliers.csv", index=False)