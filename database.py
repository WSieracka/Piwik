import mysql.connector
from mysql.connector import Error


def data():
    """A function that creates a work1 database if it does not already exist"""
    try:
        database = mysql.connector.connect(
            host='localhost',
            user='root',
            password='password')
        if database.is_connected():
            cursor = database.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS work1")

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if database.is_connected():
            cursor.close()
            database.close()
            print("MySQL connection is closed")


data()
