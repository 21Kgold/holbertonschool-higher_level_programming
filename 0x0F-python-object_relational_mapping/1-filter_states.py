#!/usr/bin/python3
"""
Connect to MySQL database "states" remotely using python’s MySQLdb module
and lists all states with a name starting with N
"""

import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = connection.cursor()
    select_query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                    ORDER BY id ASC;"
    cursor.execute(select_query)
    for row in cursor.fetchall():
        print(row)
    connection.close()
