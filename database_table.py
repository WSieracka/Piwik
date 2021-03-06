import mysql.connector
from mysql.connector import Error


def dtable():
    """Function that creates tables for the work1 database"""
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='work4',
                                             user='root',
                                             password='password')
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS employees(emp_no INT NOT NULL, birth_date DATE NOT NULL, first_name "
                "VARCHAR(14) NOT NULL, "
                "last_name VARCHAR(16) NOT NULL, gender ENUM ('M','F')  NOT NULL, hire_date DATE NOT NULL, "
                "PRIMARY KEY (emp_no))")
            cursor.execute("CREATE TABLE IF NOT EXISTS departments(dept_no CHAR(4) NOT NULL, dept_name VARCHAR(40) NOT "
                           "NULL, PRIMARY KEY (dept_no),UNIQUE  KEY (dept_name))")
            cursor.execute("CREATE TABLE IF NOT EXISTS dept_manager(emp_no INT NOT NULL, dept_no CHAR(4) NOT NULL, "
                           "from_date DATE NOT "
                           "NULL, to_date DATE NOT NULL, FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE "
                           "CASCADE, FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE, "
                           "PRIMARY KEY (emp_no,dept_no))")
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS dept_emp(emp_no INT NOT NULL, dept_no CHAR(4) NOT NULL, from_date "
                "DATE NOT NULL, "
                "to_date DATE NOT NULL, FOREIGN KEY (emp_no) REFERENCES employees (emp_no)  ON DELETE CASCADE, "
                "FOREIGN KEY (dept_no) REFERENCES departments (dept_no) ON DELETE CASCADE, PRIMARY KEY ("
                "emp_no,dept_no))")
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS titles(emp_no INT NOT NULL, title VARCHAR(50) NOT NULL, from_date "
                "DATE NOT NULL, "
                "to_date DATE, FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE, "
                "PRIMARY KEY (emp_no,title, from_date))")
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS salaries(emp_no INT NOT NULL, salary INT NOT NULL, from_date DATE "
                "NOT NULL, "
                "to_date DATE NOT NULL, FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE, "
                "PRIMARY KEY (emp_no, from_date))")
            cursor.execute("SHOW TABLES")
            for table in cursor:
                print(table)

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

dtable()