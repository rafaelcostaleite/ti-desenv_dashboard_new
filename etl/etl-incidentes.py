#import mysql.connector

#mydb = mysql.connector.connect(
#  host="localhost",
#  user="root",
#  password="root",
#  database="sandbox"
#)

#mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM tasks")

#myresult = mycursor.fetchall()

#for x in myresult:
#  print(x)

import pyodbc 
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '10.3.0.122' 
database = 'vivaz' 
username = 'app_etl' 
password = 'app_etl' 
# ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
cnxn = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()