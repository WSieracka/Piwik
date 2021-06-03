import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                          database='work',
                                          user='root',
                                          password='password')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute('Select * from titles')
        query = cursor.fetchall()
        for i in query:
            print(i)


except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

