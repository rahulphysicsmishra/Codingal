# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
HouseDF = pd.read_csv('C:/Users/Karan/Downloads/USA_Housing.csv')

# Display first few rows
HouseDF.head()

# Display dataset information
HouseDF.info()

# Display column names
HouseDF.columns

# Create pairplot
sns.pairplot(HouseDF)

# Create heatmap of correlations
sns.heatmap(HouseDF.corr(), annot=True)