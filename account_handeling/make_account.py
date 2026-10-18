from account_handeling import get_account as ga
from account_handeling import text
import os

def create_account(cur,con):
    while True:
        os.system("cls")
        account_name = input("""
        
        What account name do you want for youre account
                to go back write "back"
        
        """)

        if str.lower(account_name) == "back":
            break
        else:
            name_list = ga.get_names(cur)
            name_taken = ga.string_control(account_name,name_list)

            if name_taken == False:
                os.system("cls")
                account_password = input(f"""
                
            Hello {account_name}
         what password do you want
         
        """)

                os.system("cls")
                account_password_reapeat = input("""
            
        write youre password one more time
            
            """)
                if account_password == account_password_reapeat:
                    
                    ga.add_account(cur,con,account_name,account_password)
                    ga.fancy_print(text.account_oppend,5)
                    break

                else:
                    ga.fancy_print(text.password_dont_match,5)

            else:
                ga.fancy_print(text.name_taken,5)





#def get_posts():
#    for row in cur.execute('''SELECT * FROM storage'''):
#        print(row[2])