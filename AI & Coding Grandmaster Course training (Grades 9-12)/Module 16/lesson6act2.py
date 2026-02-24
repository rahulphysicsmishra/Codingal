####**Import Libraries**

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

# Import dataset
data = pd.read_csv('Iris.csv')

data.head(5)

"""#### **Check Null Values**"""

data.isnull().sum()

"""- No null values are present

#### **Statistical Information of features**
"""

data.describe()

"""#### **CreateBoxplot of all the features and check if outliers are present**"""

labels = ['Id','SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
for label in labels:
  print('Distribution of', label)
  sns.boxplot(data[label])
  plt.show()

"""**Conclusion**

- SepalWidthCm has outliers

#### **Check correlation between all the features**
"""

sns.heatmap(data.corr())

"""#### **Check if any feature is skewed or not**"""

labels = ['Id','SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
for label in labels:
  print('Distribution of', label)
  sns.distplot(data[label])
  plt.show()

labels = ['Id','SepalLengthCm','SepalWidthCm','PetalLengthCm','PetalWidthCm']
for label in labels:
  print('skewness of ', label)
  print(data[label].skew())