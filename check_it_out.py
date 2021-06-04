import mysql.connector
from mysql.connector import Error


def check():
    """A function that extracts data from the titles table of the work4 database. At first it connects to the
    database, then if it is connected it prints all the data from the table. If the connection fails, an error is
    printed in the terminal. At the end we disconnect. """
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='work4',
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


check()
