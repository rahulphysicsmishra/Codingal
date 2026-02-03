# Import dataset
from google.colab import files
file = files.upload()

# Connect with sqlite database
# Import necessary libraries
import sqlite3

conn = sqlite3.connect('database.sqlite')

print("Opened database successfully")

# Create a new table in given database with mentioned constraints
conn.execute('''CREATE TABLE CLASS_10
         (SNO INT PRIMARY KEY NOT NULL,
         Roll_No INT NOT NULL,
         Name TEXT NOT NULL,
         AGE INT DEFAULT (15),
         GENDER TEXT NOT NULL,
         Email_ID TEXT NOT NULL,
         Contact_No REAL NOT NULL);''')

print("Table created successfully")

# Enter data for 3 different entries
conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
      VALUES (1, 1, 'Allen', 14, 'Male', 'allen@gmail.com', 8080900 )");

conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
      VALUES (2, 2, 'Aisha', 14, 'Female', 'aish@gmail.com', 9080900 )");

conn.execute("INSERT INTO CLASS_10 (SNO,Roll_No,NAME,AGE,Gender,Email_ID,Contact_No) \
      VALUES (3, 3, 'Jeff', 15, 'Male', 'allen@gmail.com', 9900900 )");

# Save the changes
conn.commit()
print("Records created successfully")

# Display all the tables of this database
import pandas as pd
tables = pd.read_sql("""SELECT * 
                    FROM sqlite_master
                    WHERE type='table';""", conn)
tables

# Read Table from the database into dataframe
class_10d = pd.read_sql("""SELECT *
                        FROM CLASS_10;""", conn)

class_10d.head()

