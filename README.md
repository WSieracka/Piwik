# Recruitment task from Piwik company
## Table of contents
* [Used environment](#used-environment)
* [General info](#general-info)
* [Start-up](#start-up)
* [Information-about-scripts](#information)
* [Important-information](#begin)
## Used environment
PyCharm Community 2021.1
## General info
The project was created as a recruitment assignment for Piwik company.
## Start-up
1. Clone the repository
2. Go to folder: cd Piwik
3. Replace the connection options(host,database,user,password) in all files
4. Run the main script: python3 main.py
## Information-about-scripts
##main.py - run scripts that create a database, tables to a database, copies data from one database to
    another, prints table data and does unit tests.
##database.py - create a work4 database if it does not already exist.
##database_table.py - create tables for the work4 database.
##connection.py - copies the data from the titles table in the employees database to the titles table in the work4 database.
##check_it_out.py - extracts data from the titles table of the work4 database.
##ret.py - returns data from the titles table of the employees database.
##test.py - contains unit tests
##doc.zip - contains documentation
##answers.txt - includes answers to the questions
## Important-information
After running main.py, we will be asked to select a number. Each number runs the corresponding script (the scripts have already been described in the information-about-scripts)
##1. database.py
##2. database_table.py
##3. connection.py
##4. check_it_out.py
##5. test.py
