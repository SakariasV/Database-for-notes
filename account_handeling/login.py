from account_handeling import get_account as ga
import os
import time


def try_login(cur):
    os.system("cls")
    account_name = input("""
          
    What is the account name?


""")
    name_list = ga.get_names(cur)
    account_exist  = ga.string_control(account_name,name_list)
    if account_exist == True:
        os.system("cls")
        input_password = input("""

        Whats youre password?


""")
        correct_password = password_control(cur,input_password,account_name)
        if correct_password == True:
            account_data = (True,account_name,input_password)
            return account_data
        else:
            account_data = (False,account_name,input_password)
            os.system("cls")
            print("""
        Sory you got the wrong password
            try some other time
""")
            time.sleep(5)
            return account_data
    else:
        os.system("cls")
        print("""

    Cant find a account with that name
            Try another name
""")
        time.sleep(5)
        account_data = (False,account_name,"")
        return account_data

def password_control(cur,try_password, account_name):
    db_password = ga.get_password(cur,account_name)
    if try_password == db_password:
        return True
    else:
        return False