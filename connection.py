import mysql.connector
from mysql.connector import Error


def connect():
    """This function copies the data from the titles table in the employees database to the titles table in the work1
    database. Initially, we connect to both databases. When the connections are successful, the data from the
    employees table is copied to the work1 database. Then the same happens with the data from the titles table. At
    the end we disconnect. """
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='employes',
                                             user='root',
                                             password='password')
        connection2 = mysql.connector.connect(host='localhost',
                                              database='work1',
                                              user='root',
                                              password='password')
        if connection.is_connected() and connection2.is_connected():
            cursor = connection.cursor()
            cursor2 = connection2.cursor()
            cursor.execute('Select * from employees')
            query2 = cursor.fetchall()
            cursor2.executemany("insert into employees values (%s,%s,%s,%s,%s,%s);", query2)
            cursor.execute('Select * from titles')
            query3 = cursor.fetchall()
            cursor2.executemany("insert into titles values (%s,%s,%s,%s);", query3)
            connection2.commit()

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
        if connection2.is_connected():
            cursor2.close()
            connection2.close()
            print("MySQL connection is closed")


connect()
