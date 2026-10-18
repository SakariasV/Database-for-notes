import make_database
import write as w
import sqlite3
from account_handeling import menu as m
from note_handling import todo
con = make_database.con
cur = make_database.cur

while True:
    user_data = m.main_menu(cur,con)
    todo.run(cur,con,user_data)