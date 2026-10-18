from note_handling import todo_text as tt
from note_handling import work
from account_handeling import get_account as ga
import os
import time


def run(cur,con,userdata):
    while True:
        os.system("cls")
        user_input = input(f"""
                Hi {userdata[1]}

        What are you looking to do today

            1) Read notes
            2) Write note
            3) Remove note

            """)
        if user_input == "1":
            title_list = work.get_titles(cur)
            note_list = work.get_notes(cur)
            os.system("cls")
            loop_number = 0

            try:
                for title in title_list:
                    print(f"{loop_number}) {title}")
                    loop_number = loop_number + 1
            
                pick_note = input("")
                note = note_list[pick_note]
                print(note)
                time.sleep(5)

                # quit here <-------------------------------------

            
            except Exception:
                ga.fancy_print(tt.no_notes,3)

            

            
        elif user_input == "2":
            work.write_note(cur, con, userdata)
        elif user_input == "3":
            pass
        else:
            ga.fancy_print(tt.invalid_input,3)




