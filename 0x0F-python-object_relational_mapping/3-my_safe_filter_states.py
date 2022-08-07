#!/usr/bin/python3
"""
Connect to MySQL database remotely using python’s MySQLdb module,
lists all states who's name match a command line argument and
safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    match = str(sys.argv[4])
    cursor = connection.cursor()
    select_query = "SELECT * FROM states WHERE name LIKE BINARY '{}' \
                    ORDER BY id ASC".format(match)
    cursor.execute(select_query)
    for row in cursor.fetchall():
        print(row)
    connection.close()
