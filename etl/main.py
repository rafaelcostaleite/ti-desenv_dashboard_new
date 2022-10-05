import pyodbc

print("main.py - start")

#Add your own SQL Server IP address, PORT, UID, PWD and Database
conn = pyodbc.connect(
    'DRIVER={FreeTDS};SERVER=10.3.0.122;PORT=1433;DATABASE=vivaz;UID=app_etl;PWD=app_etl', autocommit=True)
cur = conn.cursor()

#This is just an example
cur.execute("SELECT @@version;") 
row = cur.fetchone() 
while row: 
    print(row[0])
    row = cur.fetchone()

cur.close()
conn.close()

print("main.py - end")