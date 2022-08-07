#!/usr/bin/python3
"""
Connect to MySQL database remotely using python’s MySQLdb module,
lists all states who's name match a command line argument and
safe from MySQL injections!
Intruders can cause major harm by performing Python SQL injection by
accesing databases executing queries, exploting code vulnerabilities,
Examples of string interpolation that should not be used ever:
"WHERE name LIKE BINARY '{}'".format(match)
f"WHERE name LIKE BINARY '{match}'"
"WHERE name LIKE BINARY '%s'"% match
WHERE name LIKE BINARY '" + match + "'"
"""

import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    match = sys.argv[4]
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s \
                    ORDER BY id ASC", (match, ))
    for row in cursor.fetchall():
        print(row)
    connection.close()
