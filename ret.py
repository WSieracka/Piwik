import mysql.connector



def check_employees():
    """Function that returns data from the titles table of the employees database"""
    connection = mysql.connector.connect(host='localhost',
                                         database='employes',
                                         user='root',
                                         password='password')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute('Select * from titles')
        query = cursor.fetchall()
        return query


def check_work():
    """Function that returns data from the titles table of the work1 database"""
    connection = mysql.connector.connect(host='localhost',
                                         database='work1',
                                         user='root',
                                         password='password')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute('Select * from titles')
        query = cursor.fetchall()
        return query
