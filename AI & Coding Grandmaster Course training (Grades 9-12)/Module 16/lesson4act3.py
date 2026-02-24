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
data = pd.read_csv('Titanic Dataset.csv')

data.head(5)

"""#### **Create new dataset with only Numerical Features**"""

num_data = data.drop(['Name', 'Ticket', 'Cabin', 'Embarked', 'Gender'], axis=1)

labels = ['PassengerId','Survived','Pclass','Age','SibSp','Parch','Fare']

"""#### **Creating boxplot for all the features**"""

for label in labels:
  plt.boxplot(num_data[label])
  print('Distribution of', label)
  plt.show()

"""**Conclusion -**

- since there are outliers present in many features, so we should standardize the features

#### **Scaling Dataset**
"""

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
num_data = scaler.fit_transform(num_data)