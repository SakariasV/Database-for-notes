import random
import os


#('''CREATE TABLE IF NOT EXISTS notes
#(key text PRIMARY KEY, name text, title text , note text)''')



def get_titles(cur):
    title_list = []
    for title in cur.execute(""" SELECT title FROM notes """):
        title_list.append(title)
    return title_list

def get_notes(cur):
    notes = []
    for note in cur.execute(""" SELECT * FROM notes"""):
        notes.append(note)
        return notes


def get_id(cur):
    id_list = []
    for id in cur.execute('''SELECT key text FROM notes'''):
        id_list.append(id)
    return id_list


def check_id(id_list,new_id):
    for id in id_list:
        if id == new_id:
            return False
    return True

def make_key(cur):
    id_list = get_id(cur)
    print(id_list)
    checking = False
    while checking == False:
        new_id = random.randint(0,10000)
        print(new_id)
        str(new_id)
        checking = check_id(id_list, new_id)
    return new_id

def uppload(cur, con, title, text, userdata):
    new_key = make_key(cur)
    cur.execute(f""" INSERT OR IGNORE INTO notes VALUES 
                        ('{new_key}','{userdata[1]}','{title}','{text}')""")
    con.commit()

def write_note(cur, con, userdata):
    os.system("cls")
    note_title = input("""

        Title off youre note

        """)
    
    os.system("cls")
    note_text = input(f"""

        {note_title}
    What do you want to write

""")

    uppload(cur, con, note_title, note_text, userdata)