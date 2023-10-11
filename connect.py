import sqlite3 as sql # import the sqlite3 module and assign it with sql as an alias

# To use the module, start by creating a database Connection object(variable):
dbCon = sql.connect("MenuEng.db") # create and/or use db if exists

# create a cursor object to connect to the database to execute sql statement/queries 
dbCursor = dbCon.cursor()