# import the connect.py module to read data from the songs table
from connect import *

# create function 
def read_data():
    
    # select all records from the songs table
    dbCursor.execute("SELECT * FROM products")

    # fetch the selected recordS and assigned it to the allRecords variable
    allRecords = dbCursor.fetchall()

    # loop through and display all records 
    for eachRecord in allRecords:
        # display each record 
        print(eachRecord)

if __name__ == "__main__":
    read_data()