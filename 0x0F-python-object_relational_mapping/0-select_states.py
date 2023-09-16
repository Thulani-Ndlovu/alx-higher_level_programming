#!/usr/bin/python3
'''script that lists all states from the database hbtn_0e_0_usa'''
import sys
import MySQLdb


def States(username, password, name):
    '''listing all the states'''
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        username=username,
        passwd=password,
        db=name
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    States(username, password, name)
