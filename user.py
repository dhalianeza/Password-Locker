#!/usr/bin/env python3.6
class User:
    """
    Class that generates new instances of  User.
    """
    user_list = [] 
    def __init__(self,user_name,password):
        self.user_name = user_name
        self.password = password

    def save_user(self):  
        '''
        save_account method saves user objects into user_list
        '''

        User.user_list.append(self)

    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a user_name and returns a user that matches that user.
        Args:
            user_name: user_name to search for
        Returns :
            user of person that matches the number.
        '''

        for user in cls.user_list:
            if user.user_name == user_name:
                return user


    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a user exists from the user list.
        Args:
            user_name: user_name to search for
            Boolean: True or false depending if the user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return True

            return False
  

        