from account_handeling import get_account as ga
from account_handeling import make_account
from account_handeling import login
from account_handeling import text
import time
import os
def main_menu(cur,con):
    while True:
    
        os.system("cls")
        option = input(text.menu)
        if option == "1":
            userdata = login.try_login(cur)
            if userdata[0] == True:
                os.system("cls")
                print(f"""

        Hello {userdata[1]}
        welcome  back

""")

                time.sleep(5)
                return userdata

        
        elif option == "2":
            make_account.create_account(cur,con)
        elif option == "3":
            ga.fancy_print(text.reset_password,5)
            pass
        else:
            ga.fancy_print(text.invalid_input,5)
            pass
