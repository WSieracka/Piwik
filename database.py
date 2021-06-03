import mysql.connector
from mysql.connector import Error

try:
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='password')
    if database.is_connected():
        cursor = database.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS work")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if database.is_connected():
        cursor.close()
        database.close()
        print("MySQL connection is closed")



