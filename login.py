#!/usr/bin/env python3.6
import random
from user import User
from credentials import Credential

def create_user_account(user_name,pass_word):
    """
    Function to create a new account
    """
    new_user = User(user_name,pass_word)
    return new_user

def create_credentials(view_password,account,login_name,pass_word):
    """
    Function to create a new credential
    """
    new_credential = Credential(view_password,account,login_name,pass_word)
    return new_credential   

def save_user_account(user):
    """
    Function to save user account
    """
    user.save_user()

def save_credentials(credential):
    """
    Function to save credentials
    """
    credential.save_credential()

def del_credential(account):
    '''
    Function to delete a credential
    '''
    account.del_credential()  

def check_existing_users(characters):
    """
    Function that checks if a user exists with those characters and retuen a boolean
    """
    return User.user_exist(characters)


def display_credentials():
     """
     Function that returns the credentials list
     """
     return Credential.display_credentials()

def find_credentials(account_name):
    '''
    Funtion that finds a credentials object and returns it
    '''
    return Credential.find_by_acc_name(account_name)


def main():
    print("Hello! Welcome to the Password Locker. What is your name?")
    u_name = input()
    print("\n")
    print(f"Hello {u_name}.what would you like to do?")
    while True:
        print("\nUse these short codes below:")
        print("*" * 30)
        print("\n ca - create an account, cc - create credentials, gp - generate password, cp - create own password, dc - display credentials, rc - delete credentials, ex - exit password locker")
        short_code = input().lower() 

        if short_code == 'ca':
            print("New account")
            print("*" * 20)

            print("\nEnter your user name")
            print("*"*20)
            user_name = input()

            print("\nEnter a password")
            print("*"*20)
            pass_word = input()

            save_user_account(create_user_account(user_name,pass_word))

            print("\n")
            print(f"New Account **{user_name}** created.\n")

        elif short_code == "cc":
            print("\nLogin to your account")
            print("*"*20)
            print("\nUsername?")
            print("*" * 20)
            username_input = input()
            print("\nPassword?")
            print("*"*20)
            user_password_input = input()
            view_password = user_password_input 
            if check_existing_users(user_password_input):
                print("\nWelcome back!")
                print("New Credential")
                print("*" *20)

                print("\nWhich account do the credentials belong to?")
                print("*"*40)
                account = input()

                print(f"\nWhat's your login name for the {account} account?")
                print("*"*40)
                login_name = input()

                print("\nChoose:")
                print("*"*20)
                print("'gp' - program to generate your password for you, 'cp' - create your own password")
                password_creation_input = input()
                if password_creation_input == "cp":
                    print("\nEnter your password")
                    print("*"*20)
                    pass_word = input()

                elif password_creation_input == "gp":
                    chars = "abcdefghijklmnopqrstuvwxyz1234567890"
                    pass_word = "".join(random.choice(chars) for _ in range(8))
                    print(f"\nYour password is: **{pass_word}**")

                save_credentials(create_credentials(view_password,account,login_name,pass_word))
                print("\n")
                print(f"New credentials **{account}**, **{login_name}**, **{pass_word}** created")



            else:

                print("Wrong password or username. Please Try again.\n Username?")
                print("*"*20)
                username_input = input()
                print("\nPassword?")
                print("*"*20)
                password_input = input()
                if check_existing_users(user_password_input):
                    print("\nWelcome back!")
                else:
                    print("You don't have an account.\n")        
               
        elif short_code == 'dc':

             if display_credentials():
                 print("Here is a list of your credentials:")
                 print("*"*40)
                 for credential in display_credentials():
                     print(f"\nAccount: {credential.account}\nLogin Name: {credential.login}\nAccount Password: {credential.password}")    
           

                
             else:
                 print("\n You don't seem to have any credentials saved yet")    

        elif short_code == 'rc':
            print("Enter the account name you want to delete")

            del_account = input()
            if check_existing_users(del_account):
                
                search_del_credential = find_credentials(del_account)
                del_credential(search_del_credential)
                         
                print(f"Deleted credentials of {del_account}")         
            else:
                print("That credential does not exist")

        elif short_code == 'ex':
            print("*"*20)
            print("Thank you for using Password Locker...")
            print("*"*40)
            break

        else:
            print("Sorry, I didn't get that. Please use the short codes\n")
        

 
 


if __name__ == '__main__':

     main()
   