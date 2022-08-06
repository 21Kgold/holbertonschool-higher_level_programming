#!/usr/bin/python3
"""
Connect to MySQL database remotely using python’s MySQLdb module
"""

# module to import MySQL
import MySQLdb
import sys

# Guard script from be executed when imported
if __name__ == "__main__":
    # Connect to database: user, passwd and database_name will be passed
    # as command line arguments and port number was provided as 3306 which
    # is the default value
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # Making Cursor Object For Query Execution using cursor() method
    cursor = connection.cursor()
    # The SELECT statement is used to select data from "states" database
    select_query = "SELECT * FROM states ORDER BY id ASC;"
    # Executing Query
    cursor.execute(select_query)
    # The fetchall() method retrieves all the rows
    for row in cursor.fetchall():
        print(row)
    # disconnect from server
    connection.close()
