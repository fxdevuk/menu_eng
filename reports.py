# import the connect.py module to read data from the songs table
from connect import *

# # create function 
def report():
    
#     # select all records from the products table
#     # dbCursor.execute("SELECT * FROM products")
#     # dbCursor.execute("SELECT * FROM products ORDER BY productID DESC")
#     # dbCursor.execute("SELECT Artist, Genre  FROM products")
#     # dbCursor.execute("SELECT * FROM products WHERE Genre = 'Rap' or  Genre = 'Pop' ")
#     # dbCursor.execute("SELECT * FROM products ORDER BY Artist ASC")
#     # dbCursor.execute("SELECT * FROM products WHERE Title LIKE 'B%' ")
#     # dbCursor.execute("SELECT * FROM products WHERE Artist LIKE '%O%' ")
#     # dbCursor.execute("SELECT * FROM products WHERE Artist NOT LIKE '%O%' ")


    # fetch the selected recordS and assigned it to the allRecords variable
    allRecords = dbCursor.fetchall()

    # loop through and display all records 
    for eachRecord in allRecords:
        # display each record 
        print(eachRecord)


def reportSearch():
    titleValue = input("Enter the Song Title to search for: ")
    dbCursor.execute(f"SELECT * FROM songs WHERE Title = '{titleValue}' ")

    # fetch the selected recordS and assigned it to the allRecords variable
    allRecords = dbCursor.fetchall()

    # loop through and display all records 
    for eachRecord in allRecords:
        # display each record 
        print(eachRecord)

if __name__ == "__main__":
    report()
    reportSearch()