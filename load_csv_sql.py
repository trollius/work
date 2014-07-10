import csv
import sqlite3

# Create the database
connection = sqlite3.connect('test.db')
connection.text_factory = str
cursor = connection.cursor()

# Create the table
cursor.execute('DROP TABLE IF EXISTS prices')
cursor.execute('CREATE TABLE  prices ( myid integer, parent_id integer, hlevel integer, name text, description text, publications text, tool_ver text) ')
connection.commit()

# Load the CSV file into CSV reader
csvfile = open('mytools.txt', 'rb')
creader = csv.reader(csvfile, delimiter=';', quotechar='|')

# Iterate through the CSV reader, inserting values into the database
for t in creader:
    cursor.execute('INSERT INTO  prices VALUES (?,?,?,?,?,?,?)', t )

# Close the csv file, commit changes, and close the connection
csvfile.close()
connection.commit()
connection.close()

#myid,parent_id,hlevel,name,description,publications,tool_ver