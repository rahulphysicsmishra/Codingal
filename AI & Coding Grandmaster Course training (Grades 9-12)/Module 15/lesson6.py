# Load Basic Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Reading the csv file
df = pd.read_csv("heart.csv")

# Display first few rows
df.head()

# Display dataset shape
df.shape

# Display column names
df.columns

# Display descriptive statistics
df.describe()

# Check for null values
df.isnull().sum()

# Display dataset information
print(df.info())

# Create histograms
df.hist(figsize=(12,12), layout=(5,3))

# Create box and whiskers plots
df.plot(kind='box', subplots=True, layout=(5,3), figsize=(12,12))
plt.show()

# Create barplot
sns.barplot(data=df, x='sex', y='chol', hue='target', palette='spring')

# Display value counts for sex column
df['sex'].value_counts()

# Display value counts for target column
df['target'].value_counts()

# Display value counts for thal column
df['thal'].value_counts()

# Create correlation heatmap
plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot=True, cmap='terrain')

# Create countplot for sex vs target
sns.countplot(x='sex', data=df, palette='husl', hue='target')

# Create countplot for target
sns.countplot(x="target", palette="BuGn", data=df)

# Create countplot for ca vs target
sns.countplot(x="ca", hue="target", data=df)