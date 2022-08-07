#!/usr/bin/python3
"""
Lists "id" from table "cities" + "name" from table "cities" + "name" from table
"states". Both tables frome database hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    match = sys.argv[4]
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name FROM cities JOIN states ON \
                    cities.state_id = states.id WHERE states.name LIKE \
                    BINARY %s ORDER BY cities.id ASC;", (match, ))
    for row in cursor.fetchall():
        print(row)
    connection.close()
