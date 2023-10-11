# import the connect.py module to read data from the songs table
from connect import *

# create function 
def update_data():
    # use primary key to update a record

    idField = input("Enter ProductID of the record to be updated: ")

    # field to be updated
    fieldName = input("Enter name of product as field name").title()

    # field value : ask for the for the Title or Artist or Genre to be updated
    fieldValue = input(f"Enter the value for the {fieldName} field: ")

    fieldValue = "'"+fieldValue+"'"   #  add single quotes around the field value (string)

    # update record
    dbCursor.execute(F"UPDATE product SET {fieldName} = {fieldValue} WHERE ProductID = {idField}")

    dbCon.commit()

    print(f"Record {idField} updated in the products table: ")


if __name__ == "__main__":
    update_data()