# import the connect.py module to add data in the songs table
from connect import *

# create a function 
def insert_data():
    # Note: SongID is set to autoincrement, input/data is not required

    # ask for user input
    productName = input("Enter product name: ")
    productCost = input("Enter product cost: ")
    productPrice = input("Enter product sale price: ")
    productSales = input("Enter number of units sold: ")

    dbCursor.execute("INSERT INTO products(productName, productCost, productPrice, productSales) VALUES(?,?,?,?)",(productName,productCost,productPrice,productSales))
    # or 
    # dbCursor.execute("INSERT INTO songs VALUES(NULL, ?,?,?)",(songTitle,songArtist,songGenre))
    dbCon.commit() # permanently write the data in the songs table in the database

    print(f"{productName} inserted into the Products table")

#  if __name__ == "__main__": will prevent the functions/method from running
#  automatically when the file is imported in another file
if __name__ == "__main__":
    insert_data()
