import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='743326Levin'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE fairy")

print('All done!')
