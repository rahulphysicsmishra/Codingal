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
data = pd.read_csv('Weather Dataset.csv')

data.head(5)

data.info()

"""####**Check Null Values**"""

data.isnull().sum()

"""**No feature has any null values**

#### **Mean, Variance and Standard Deviation of Temperature (C)**
"""

mean_temp = np.mean(data['Temperature (C)'])
print("Mean Temperature is :", mean_temp)

var_temp = np.var(data['Temperature (C)'])
print("Variation of Temperature is :", var_temp)

standard_deviation_temp = np.std(data['Temperature (C)'])
print("Standard Deviation of Temperature is :", standard_deviation_temp)

"""#### **Mean, Variance and Standard Deviation of Temperature (C) for every month**"""

for i in range(1, 13):
  month = data.loc[data["month"] == i]["Temperature (C)"]
  print("For month "+str(i))
  print("Mean temperature is "+ str(np.mean(month)))
  print("Standard deviation is "+ str(np.std(month))+"\n")