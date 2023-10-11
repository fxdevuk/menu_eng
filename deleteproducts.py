# import the connect.py module to read data from the songs table
from connect import *

# create function 
def delete_data():
        # use primary key to delete a record
        idField = input("Enter the ProductID of the record to be deleted: ")

        # delete from the songs where the songid is 1/2/3/4/5......
        dbCursor.execute(f"DELETE FROM Products WHERE ProductID = {idField}")
        dbCon.commit()

        print(f"Record {idField} deleted from the Products table")
if __name__ == "__main__":
        delete_data()
