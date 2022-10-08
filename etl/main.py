import configparser
import pyodbc
import mysql.connector

print("main.py - start")

config = configparser.ConfigParser()
config.sections()
config.read('./config.ini')

#print(config['sqlserver']['server'])

#Add your own SQL Server IP address, PORT, UID, PWD and Database
conn = pyodbc.connect(
    #'DRIVER={FreeTDS};SERVER=10.3.0.122;PORT=1433;DATABASE=vivaz;UID=app_etl;PWD=app_etl'
    'DRIVER={FreeTDS};SERVER='+config['sqlserver']['server']+';\
        PORT='+config['sqlserver']['port']+';\
            DATABASE='+config['sqlserver']['database']+';\
                UID='+config['sqlserver']['login']+';\
                    PWD='+config['sqlserver']['password']+''
    , autocommit=True
)

cur = conn.cursor()

#This is just an example
cur.execute("SELECT @@version ;") 
row = cur.fetchone() 
while row: 
    print(row[0])
    row = cur.fetchone()

cur.close()
conn.close()

print("main.py - mysql")

mydb = mysql.connector.connect(
  host=config['mysql']['host']
  ,user=config['mysql']['user']
  ,password=config['mysql']['password']
)

print(mydb)

print("main.py - end")