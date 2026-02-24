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

"""####**Check Null Values**"""

data.isnull().sum()

"""**Null values present in Cabin -**

#### **Quartiles of Feature Age**
"""

age_q1 = np.quantile(data['Age'], 0.25)
age_q2 = np.quantile(data['Age'], 0.50)
age_q3 = np.quantile(data['Age'], 0.75)

print("Age Quartiles -")
print("Q1 -", age_q1)
print("Q2 -", age_q2)
print("Q3 -", age_q3)

"""#### **Interquartile Range of Feature Age**"""

IQR_age = age_q3 - age_q1
print("Interquartile Range :", IQR_age)

"""#### **Plot Histogram for feature Age**"""

plt.hist(data['Age'])
plt.ylabel("Count of Passengers")
plt.xlabel("Age")

"""#### **Quartiles for feature Fare**"""

fare_q1 = np.quantile(data['Fare'], 0.25)
fare_q2 = np.quantile(data['Fare'], 0.50)
fare_q3 = np.quantile(data['Fare'], 0.75)

print("Fare Quartiles -")
print("Q1 -", fare_q1)
print("Q2 -", fare_q2)
print("Q3 -", fare_q3)

"""#### **Interquartile Range of Feature Fare**"""

IQR_fare = fare_q3 - fare_q1
print("Interquartile Range :", IQR_fare)

"""#### **Plot histogram for feature Fare**"""

bins =np.arange(0,250,20)
plt.hist(data['Fare'], bins=np.arange(1,250, 20))
plt.ylabel("Count of Passengers")
plt.xlabel("Fare")
plt.xticks(bins)