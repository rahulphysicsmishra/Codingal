import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

Titanic = pd.read_csv(r"Titanic.csv")
Titanic.head()

Titanic.shape

Titanic.isnull().sum()

sns.heatmap(Titanic.isnull(), cmap="spring")

#Since the highest null values are found in "deck" coloumn so dropping it respectively..

#Printing the original Dataset again

Titanic.head()

#Dropping the deck coloumn

Titanic.drop("deck", axis=1, inplace=True)

#Printing the Dataset after dropping the coloumn

Titanic.head()

Titanic.dropna(inplace=True)

sns.heatmap(Titanic.isnull(), cbar=False)

#As you can see no null values found

#Now all the null values have been removed "CHECK"

Titanic.isnull().sum()

#Simplifying the data more by converting the string data types to integer.

pd.get_dummies(Titanic["sex"]).head()

sex = pd.get_dummies(Titanic["sex"], drop_first=True)

sex.head(4)

#If we observe embark_town there are only two data types present which can be split in the form of integers

pd.get_dummies(Titanic["embarked"]).head(4)

arked = pd.get_dummies(Titanic["embarked"], drop_first=True)

#Similarly for pclass

pclass = pd.get_dummies(Titanic["pclass"], drop_first=True)

pclass.head(4)

Titanic = pd.concat([Titanic, sex, pclass], axis=1)

#Printing the Updated Dataset
Titanic.head()