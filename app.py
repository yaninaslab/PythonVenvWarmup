import dbinteractions as dbi
import getpass as gp

username = input("Please enter your username: ")
password = gp.getpass("Please enter your password: ")

login_success, user_id = dbi.attempt_login(username, password)

if(login_success == True):
    dbi.list_your_dogs(user_id)
    #print("Authentication success!")

else:
    print("Sorry, authentication failure")
    exit()
