#!/usr/bin/python3
"""
Lists "name" from table "cities" that match with command line "name" from
table "states". Both tables frome database hbtn_0e_4_usa
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
    list_of_cities = ""
    for row in cursor.fetchall():
        for city in row:
            list_of_cities += f"{city}, "
    print(list_of_cities[:-2])
    connection.close()
