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
    cursor = connection.cursor()
    select_query = "SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC;"
    cursor.execute(select_query)
    for row in cursor.fetchall():
        print(row)
    connection.close()
