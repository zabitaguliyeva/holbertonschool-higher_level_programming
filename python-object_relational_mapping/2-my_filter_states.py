#!/usr/bin/python3
"""
Filter states by user input
"""

import MySQLdb
import sys

if __name__ == "__main__0":
    db = MySQLdb.connect(
        host = "localhost",
        port = 3306,
        user = sys.argv[1],
        password = sys.argv[2],
        db = sys.argv[3],
        searched = sys.argv[4]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
               ORDER BY id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
