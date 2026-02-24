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

"""#### **Passengers belonging from which gender survived the most**"""

sns.countplot(data['Gender'], hue=data['Survived'])

"""#### **Passengers belonging from which PClass survived the most and the least**"""

sns.countplot(data['Pclass'], hue=data['Survived'])

"""#### **Highest number of passengers belong to which Age**"""

sns.distplot(data['Age'],kde=False,bins=40)

"""#### **Highest number of passengers belong to which Gender**"""

sns.countplot(data['Gender'])

"""#### **Is SibSp correlated/associated with Survived feature**"""

sns.countplot(x='Survived', hue='SibSp', data=data, palette="mako")

"""#### **Is Parch correlated/associated with Survived feature**"""

sns.countplot(x='Survived', hue='Parch', data=data, palette="mako")

"""#### **Is the feature Fare having normal distribution/spread of data**"""

sns.distplot(data['Fare'])
plt.show()

"""#### **Check the age group of majority of people belonging to PClass=1**"""

sns.boxplot(x='Pclass',y='Age',data=data,palette='winter')

"""#### **Check the correlation of all the features with target variable ‘Survived’**"""

sns.heatmap(data.corr())