# Import Dataset
from google.colab import files
uploaded = files.upload()

# Import Necessary Libraries
import numpy as np
import pandas as pd
import sqlite3

# Setup connection with database 
# And display all tables inside the database
database = 'database.sqlite'

conn = sqlite3.connect(database)

tables = pd.read_sql("""SELECT *
                        FROM sqlite_master
                        WHERE type='table'""", conn)

tables

# Check how Inner join works
joined_city = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                            FROM country c
                            INNER JOIN city ci
                            ON c.Country_Id == ci.Country_id""", conn)
joined_city

# Check how Outer join works
joined_left = pd.read_sql("""SELECT *
                            FROM player
                            LEFT JOIN season
                            ON player.Player_Id == season.Man_of_the_Series""", conn)
joined_left

# Check how Cross join works
joined_cross = pd.read_sql("""SELECT c.Country_Id, c.Country_Name, ci.City_Name
                            FROM country c
                            CROSS JOIN city ci""", conn)
joined_cross

# Check how Union Clause works
union = pd.read_sql("""SELECT Player_Name 
                      FROM player
                      UNION
                      SELECT Team_Name
                      FROM team""", conn)

union
