import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from sklearn.preprocessing import MinMaxScaler, StandardScaler


# Load your dataset into a pandas DataFrame
df = pd.read_csv("measures.csv")

# Calculate the mean of the "stator_winding" attribute
mean_stator_winding = df['stator_winding'].mean()

# Replace missing values for "stator_winding" with the mean
df['stator_winding'].fillna(mean_stator_winding, inplace=True)

# Save the preprocessed data to a new CSV file
df.to_csv("preprocessed_data.csv", index=False)


# Load your dataset into a pandas DataFrame
df = pd.read_csv("preprocessed_data.csv")

# Select the columns you want to normalize
columns_to_normalize = ["stator_winding", "stator_tooth", "stator_yoke", "coolant"]

# Create a Min-Max scaler
scaler_minmax = MinMaxScaler()

df[columns_to_normalize] = scaler_minmax.fit_transform(df[columns_to_normalize])

# Create a StandardScaler for Z-score standardization
scaler_zscore = StandardScaler()

# Normalize the "torque" column using Z-score standardization
df["torque"] = scaler_zscore.fit_transform(df[["torque"]])

# Save the preprocessed data to a new CSV file
df.to_csv("new_preprocessed_dataset.csv", index=False)

# Create a scatter matrix plot
columns_to_include = ["stator_winding", "stator_tooth", "coolant", "torque", "stator_yoke"]
scatter_matrix(df[columns_to_include], alpha=0.5, figsize=(10, 10), diagonal='hist')
plt.show()