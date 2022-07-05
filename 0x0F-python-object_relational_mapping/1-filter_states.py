#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db_connection = MySQLdb.connect(
        host=("localhost"),
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    curso = db_connection.cursor()
    curso.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = curso.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    curso.close()
    db_connection.close()
