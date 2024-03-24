#!/usr/bin/python3
"""
Filter states
"""

import MySQLdb
import sys


if __name__ == "main":

    db = MySQLdb.connect(
            host="localhost",
            username = sys.argv[1],
            password = sys.argv[2], 
            db = sys.argv[3],
            port = 3306
            )

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC""")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    db.close()
