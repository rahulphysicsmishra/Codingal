# Import Pandas and Matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Upload File and Make a Copy of the File
countries_df = pd.read_csv('countries.csv')
countries = countries_df
countries.head(3)

# Extract the rows where the year is 1952
c_52 = countries.loc[countries['year'] == 1952]
c_52.head()

# Extract the rows where the year is 2007
c_07 = countries.loc[countries['year'] == 2007]
c_07.head()

type(c_52)

# Merge the '52 and the '07 dataframes together
c_merge = c_52.merge(c_07, left_on='country', right_on='country')
c_merge.head()

# Drop both the year columns
c_merge.drop(['year_x', 'year_y'], axis=1)
c_merge.head()

# Create a new column that takes the difference between the population_y and the population_x column
c_merge['population_growth'] = c_merge['population_y'] - c_merge['population_x']
c_merge.head()

# Test the math
31889923 - 8425333

c_merge.shape, type(c_merge)

# Sort the values so you get back the 10 countries with the biggest population growth
c_merge = c_merge.sort_values('population_growth', ascending=False).head(10)
c_merge.head(10)

# Now lets plot our data!
names = ['China', 'India', 'United States', 'Indonesia', 'Brazil', 'Pakistan', 'Bangladesh', 'Nigeria', 'Mexico', 'Philippines']
pop_grow = (c_merge['population_growth'] / 10**6)

plt.figure(figsize=(15,9))
plt.bar(names,pop_grow,width=0.6)
plt.xlabel('Country')
plt.ylabel('Population Growth (Millions)')
plt.title('Top 10 Countries w/the Biggest Population Growth from 1952 to 2007')
plt.xticks(rotation=45)

# zip joins x and y coordinates in pairs
for x,y in zip(names,pop_grow):
    label = "({:.2f}".format(y)
    
    plt.annotate(label, # this is the text
                (x,y), # this is the point to label
                textcoords="offset points", # how to position the text
                xytext=(0,10), # distance from text to points (x,y)
                ha='center') # horizontal alignment can be left, right or center

plt.show()