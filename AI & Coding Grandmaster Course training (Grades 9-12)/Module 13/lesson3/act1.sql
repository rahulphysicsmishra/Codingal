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

# Read Table from the database into dataframe
matches = pd.read_sql("""SELECT *
                        FROM Match;""", conn)

matches.head()

"""**Conclusion -**

- 12 Numeric features (Integer and Numeric) and 1 categorical feature (Text)
- 3 columns with null values
"""

# Get the Average Win Margin of all the winning teams for Season 9
result1 = pd.read_sql("""SELECT AVG(Win_Margin), Match_Winner
                        FROM Match
                        WHERE Season_Id == 9
                        GROUP BY Match_Winner
                        ORDER BY AVG(Win_Margin);""", conn)
result1

# Get the count of the venues for Season 9
result2 = pd.read_sql("""SELECT COUNT(DISTINCT Venue_Id)
                        FROM Match
                        WHERE Season_Id == 9;""", conn)
result2

# Get the Minimum, Maximum and Average Win Margin
# Also get the total number of players who have received man of the match throughout all the seasons
result3 = pd.read_sql("""SELECT MIN(Win_Margin), Max(Win_Margin), Avg(Win_Margin), COUNT(DISTINCT(Man_of_the_Match))
                        FROM Match;""", conn)
result3

# Return total of win_margins for all the winners in season 9
result4 = pd.read_sql("""SELECT SUM(Win_Margin)
                        FROM Match
                        WHERE Season_Id == 9;""", conn)
result4

