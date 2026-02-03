#### **1. Import Database**
"""

# Import file from your system
from google.colab import files
file = files.upload()

"""#### **2. Connect with SQLite Database**"""

# Connect with sqlite database
# Import necessary libraries
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

# Read SQL query for getting all the tables of database into a dataframe
import pandas as pd
tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
tables

# Check team id of all teams
teams = pd.read_sql("""SELECT *
                        FROM Team;""", conn)
teams

# Read Table from the database into dataframe
matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)

"""**Conclusion -**

- 12 Numeric features (Integer and Numeric) and 1 categorical feature (Text)
- 3 columns with null values
"""

matches

# Check details of all the matches won by Mumbai Indians
MI_wins = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner == 7;""", conn)
MI_wins

# Check details of all the matches won by Mumbai Indians in last two seasons
MI_S8_S9 = pd.read_sql("""SELECT *
                        FROM Match
                        WHERE Match_Winner == 7 and Season_Id IN (8,9);""", conn)
MI_S8_S9

new_teams = pd.read_sql("""SELECT *
                        FROM Team
                        WHERE Team_Name LIKE 'De%';""", conn)
new_teams

# Check the minimum and maximum win_margin of all the matches 
min_max_margin = pd.read_sql("""SELECT MIN(Win_Margin), MAX(Win_Margin)
                        FROM Match;""", conn)
min_max_margin

