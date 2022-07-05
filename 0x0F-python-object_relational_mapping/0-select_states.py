#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db_connection = MySQLdb.connect(host="localhost",
                                    port=3306, user=argv[1],
                                    passwd=argv[2], db=argv[3])

    curso = db_connection.cursor()
    curso.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = curso.fetchall()
    for row in query_rows:
        print(row)
    curso.close()
    db_connection.close()
