#!/usr/bin/env python3.6
import unittest 
from user import User 

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''  
    def setUp(self):
       '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("nyiraneza","dalia") 

        
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
      
        self.assertEqual(self.new_user.user_name,"nyiranezadalia")
        self.assertEqual(self.new_user.password,"dalia")  

    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1) 

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("dalia","nyiraneza","nyiranezadalia","dalia") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []    

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("dalia","nyiraneza","nyiranezadalia","dalia") 
        test_user.save_user()
        self.assertEqual(len(User.user_list),2) 

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("dalia","nyiraneza","nyiranezadalia","dalia") 
        test_user.save_user()

        self.new_user.delete_user()
        self.assertEqual(len(User.user_list),1)   
          
    def test_find_user_by_user_name(self):
        '''
        test to check if we can find a user by user_name  and display information
        '''

        self.new_user.save_user()
        test_user = User("dalia","nyiraneza","nyiranzadalia","dalia") 
        test_user.save_user()

        found_user = User.find_by_user_name("nyiranezadalia")

        self.assertEqual(found_user.user_name,test_user.user_name)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the contact.
        '''

        self.new_user.save_user()
        test_user = User("dalia","nyiraneza","nyiranezadalia","dalia") 
        test_user.save_user()

        user_exists = User.user_exist("nyiranezadalia")

        self.assertTrue(user_exists)    
      
         
       
       
        

if __name__ == '__main__':
    unittest.main()          
       
        