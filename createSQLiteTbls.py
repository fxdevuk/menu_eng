from connect import * # import the connect.py module 

dbCursor.execute(""" 
CREATE TABLE "members" (
	"MemberID"	INTEGER NOT NULL UNIQUE,
    "Menuname" TEXT,
	"Firstname"	TEXT,
	"Lastname"	TEXT,
	"Email"	TEXT,
	PRIMARY KEY("MemberID" AUTOINCREMENT)
)""")

# ...............................
dbCursor.execute("""
CREATE TABLE "products" (
	"ProductID"	INTEGER NOT NULL UNIQUE,
    "productName"	TEXT,
	"productCost"	REAL,
	"productPrice"	REAL,
	"productSales"	INT,
	PRIMARY KEY("ProductID" AUTOINCREMENT)
)""")
