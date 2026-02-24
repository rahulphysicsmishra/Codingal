####**Import Libraries**

# Import Libraries
import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

"""####**Import Dataset**"""

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Titanic Dataset.csv')

data.head()

"""####**Median Value of Age and Fare**"""

median_age = np.median(data['Age'])
print("Median value of Age -", median_age)

median_fare = np.median(data['Fare'])
print("Median value of Fare -", median_fare)

"""####**Mode Value of Age and PClass**"""

mode_age = stats.mode(data['Age'])
print("Mode value of Age -", mode_age)

mode_class = stats.mode(data['Pclass'])
print("Mode value of PClass -", mode_class)

"""####**Mode Value of Categorical Feature - Gender**"""

mode_gender = data['Gender'].value_counts().index[0]
print("Mode of Feature Gender -", mode_gender)