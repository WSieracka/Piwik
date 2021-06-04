import mysql.connector
from mysql.connector import Error
import tracemalloc
import time


def time_s():
    """Function for measuring program execution time"""
    tracemalloc.stop()
    tracemalloc.start()
    print("Tracing Status : ", tracemalloc.is_tracing())


def mem():
    """Function for measuring size and peak size of memory blocks"""
    first_size, first_peak = tracemalloc.get_traced_memory()
    peak = first_peak / (1024 * 1024)
    print("Peak Size in MB - ", peak)


def connect():
    """This function copies the data from the titles table in the employees database to the titles table in the work1
    database. Initially, we connect to both databases. When the connections are successful, the data from the
    employees table is copied to the work1 database. Then the same happens with the data from the titles table. At
    the end we disconnect. """
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='employees',
                                             user='root',
                                             password='password')
        connection2 = mysql.connector.connect(host='localhost',
                                              database='work4',
                                              user='root',
                                              password='password')
        if connection.is_connected() and connection2.is_connected():
            time_s()
            start = time.time()
            cursor = connection.cursor()
            cursor2 = connection2.cursor()
            cursor.execute('Select * from employees')
            query2 = cursor.fetchall()
            cursor2.executemany("insert into employees values (%s,%s,%s,%s,%s,%s);", query2)
            cursor.execute('Select * from titles')
            query3 = cursor.fetchall()
            cursor2.executemany("insert into titles values (%s,%s,%s,%s);", query3)
            connection2.commit()
            end = time.time()
            print("Time: {} milli seconds".format((end - start) * 1000))
            mem()

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
