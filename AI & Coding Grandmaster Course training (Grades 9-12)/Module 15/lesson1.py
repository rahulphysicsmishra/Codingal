# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from CSV file
df = pd.read_csv("country_vaccinations.csv")

# Display first 10 rows
df.head(10)

# Check for any null values in each column
df.isnull().any()

# Visualize missing values using a heatmap (optimize by using a subset of data)
subset = df.iloc[:5200, :]  # Taking the first 100 rows for better performance
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()

# Display first 10 rows
df.head(10)

# Drop rows where all values are NaN
df.dropna(how="all")

# Fill missing values using backward fill method
df.fillna(method="bfill")

# Interpolate missing values
df.interpolate()

# Drop all rows with any NaN values
df_dropped = df.dropna()
df_dropped