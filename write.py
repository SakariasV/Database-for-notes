import sqlite3
import random



def get_id(cur):
    id_list = []
    for id in cur.execute('''SELECT key text FROM storage'''):
        id_list.append(id)
    return id_list


def check_id(id_list,new_id):
    for id in id_list:
        if id == new_id:
            return False
    return True

def make_id(cur):
    id_list = get_id(cur)
    print(id_list)
    checking = False
    while checking == False:
        new_id = random.randint(0,10000)
        print(new_id)
        str(new_id)
        checking = check_id(id_list, new_id)
    return new_id



def write(cur):
    id = make_id(cur)
    name = input("Whats youre name\n")
    title = input("Title off poast\n")
    body = input("What do you want to post today\n")


    cur.execute(f'''INSERT OR IGNORE INTO storage VALUES
                        ('{id}', '{name}', '{title}', '{body}')''')