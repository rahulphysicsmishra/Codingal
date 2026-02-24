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

"""#### **Set Plot Style**"""

sns.set_style('whitegrid')

"""#### **Countplot for feature 'Survived'**"""

sns.countplot(x='Survived', data=data)

"""#### **Barchart for showing passengers belonging to different gender who survived or not**

"""

sns.countplot(x='Gender', hue='Survived', data=data)

"""#### **Customize Plots**"""

sns.countplot(x='Survived', data=data, palette='winter')

sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')

"""#### **Countplot for Embarked**"""

sns.countplot(x='Embarked', data=data)

"""#### **Rotate the value labels and modify their font size**

"""

sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=20)
plt.show()

