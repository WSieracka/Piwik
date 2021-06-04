from subprocess import call

"""@package docstring
@author Weronika Sieracka
Documentation for menu.
"""
print("1. Database creation")
print("2. Creating a table for a database")
print("3. Copying data from one table to another")
print("4. Print data from new table")
print("5. Unit test")
print("6. End")


def switch_demo(argument):
    """Function that runs scripts that create a database, tables to a database, copies data from one database to
    another, prints table data and does unit tests.
        """
    if argument == 1:
        call(["python3", "database.py"])
    if argument == 2:
        call(["python3", "database_table.py"])
    if argument == 3:
        call(["python3", "connection.py"])
    if argument == 4:
        call(["python3", "check_it_out.py"])
    if argument == 5:
        call(["python3", "test.py"])


def menu():
    """Retrieves information from the user which script to run and passes this selection to the switch_demo()
    function """
    while True:
        a = int(input("Choose a number: "))
        if a == 6:
            return False
        else:
            switch_demo(a)


menu()
