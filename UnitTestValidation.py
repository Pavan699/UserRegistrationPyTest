'''
@Author: Pavan Nakate
@Date: 2021-11-13 10:22
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : To solve unit test cases for user details. 
'''
from InfoValidation import Validation
import unittest

class UserValidationTest(unittest.TestCase):
    """
    Description:
        This Class having Functions to check the unittests for the firstname
    """  
    def test_ValidFirstName(self):
        """
        Description: 
            In this test case when given a valid first name should return true.
        """        
        self.assertTrue(Validation.validate_first_name("Pavan"))
        self.assertTrue(Validation.validate_first_name("Jay"))


    def test_InvalidFirstName(self):
        """
        Description: 
            In this test case when given a invalid first name should return false.
        """        
        self.assertFalse(Validation.validate_first_name("rahul"))
        self.assertFalse(Validation.validate_first_name("sai"))
        self.assertFalse(Validation.validate_first_name("26viru"))

    def test_ValidLastName(self):
        """
        Description: 
            In this test case when given a valid last name should return true.
        """        
        self.assertTrue(Validation.validate_last_name("Nakate"))
        self.assertTrue(Validation.validate_last_name("Mane"))

    
    def test_InvalidLastName(self):
        """
        Description: 
            In this test case when given a invalid last name should return false.
        """        
        self.assertFalse(Validation.validate_first_name("nakate"))
        self.assertFalse(Validation.validate_first_name("Mane12"))

if __name__ == '__main__':
    unittest.main()