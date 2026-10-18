import sqlite3

con = sqlite3.connect('notes.db')
cur = con.cursor()


def create():
    cur.execute('''CREATE TABLE IF NOT EXISTS notes
                        (key text PRIMARY KEY, name text, title text , note text)''')

    cur.execute('''CREATE TABLE IF NOT EXISTS accounts
                        (name text PRIMARY KEY, password)''')


create()
