import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="sandbox"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tasks")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)