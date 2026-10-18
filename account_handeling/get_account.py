import time
import os

def get_names(cur):
    name_list = []
    for row in cur.execute('''SELECT name FROM accounts'''):
        name_list.append(row)
    
    return name_list

def get_password(cur,account):
    for row in cur.execute('''SELECT * FROM accounts'''):
        if row[0] == account:
            return row[0]

def string_control(string,list):
    for item in list:
        new_item = clean_item(str(item))
        if string == new_item:
            return True
    return False

def fancy_print(str,sleep_time):
    os.system("cls")
    print(str)
    time.sleep(sleep_time)

def add_account(cur,con,name,password):
    cur.execute(f'''INSERT OR IGNORE INTO accounts VALUES
                        ('{name}', '{password}') ''')
    con.commit()

def clean_item(item):
    clean = item
    clean = clean.replace(",","")
    clean = clean.replace("(","")
    clean = clean.replace(")","")
    clean = clean.replace("'","")
    return clean