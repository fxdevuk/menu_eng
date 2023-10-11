# import the connect.py module to read data from the songs table
from connect import *

# # create function 
# def report():
    
#     # select all records from the songs table
#     # dbCursor.execute("SELECT * FROM songs")
#     # dbCursor.execute("SELECT * FROM songs ORDER BY SongID DESC")
#     # dbCursor.execute("SELECT Artist, Genre  FROM songs")
#     # dbCursor.execute("SELECT * FROM songs WHERE Genre = 'Rap' or  Genre = 'Pop' ")
#     dbCursor.execute("SELECT * FROM Products ORDER BY productName ASC")
#     # dbCursor.execute("SELECT * FROM songs WHERE Title LIKE 'B%' ")
#     # dbCursor.execute("SELECT * FROM songs WHERE Artist LIKE '%O%' ")
#     # dbCursor.execute("SELECT * FROM songs WHERE Artist NOT LIKE '%O%' ")

#     # fetch the selected recordS and assigned it to the allRecords variable
#     allRecords = dbCursor.fetchall()

#     # loop through and display all records 
#     for eachRecord in allRecords:
#         # display each record 
#         print(eachRecord)

def reportSearch():
    titleValue = input("Enter the product name to search for: ")
    dbCursor.execute(f"SELECT * FROM Products WHERE productName = '{titleValue}' ")

    # fetch the selected recordS and assigned it to the allRecords variable
    allRecords = dbCursor.fetchall()
    found = False
    # loop through and display all records 
    for eachRecord in allRecords:
        found = True
        # display each record 
        print(eachRecord)
    if not found:
        print("\nProduct not found!\n")

# if __name__ == "__main__":
#     report()
#     reportSearch()