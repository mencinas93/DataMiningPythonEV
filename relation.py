import pandas as pd

# Read your CSV file into a DataFrame (assuming your file is named 'your_data.csv')
df = pd.read_csv('Final2.csv')

# Calculate the correlation coefficient between 'Ambient Temperature' and 'Motor Temperature'
correlation_coefficient = df['ambient'].corr(df['AvgStatorTemp'])

# Print the correlation coefficient
print("Correlation Coefficient:", correlation_coefficient)