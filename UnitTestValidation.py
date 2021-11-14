'''
@Author: Pavan Nakate
@Date: 2021-11-13 10:22
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : To solve unit test cases for user details. 
'''
from InfoVAlidation import Validation
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

    def test_ValidMobileNumber(self):
        """
        Description: 
            In this test case when given a valid mobile number should return true.
        """        
        self.assertTrue(Validation.validate_mobile("91 9960748875"))
        
    
    def test_InvalidMobileNumber(self):
        """
        Description: 
            In this test case when given a invalid mobile number should return false.
        """        
        self.assertFalse(Validation.validate_mobile("88 9451457854"))
        self.assertFalse(Validation.validate_mobile("9198564"))

    def test_ValidPassword(self):
        """
        Description: 
            In this test case when given a valid password should return true.
        """        
        self.assertTrue(Validation.validate_password("Abc$123d"))
        self.assertTrue(Validation.validate_password("Pavan#18"))


    def test_InvalidPassword(self):
        """
        Description: 
            In this test case when given a invalid password should return false.
        """        
        self.assertFalse(Validation.validate_password("sfdgs8hga"))
        self.assertFalse(Validation.validate_password("AWEFAG$45"))

    def test_ValidEmail(self):
        """
        Description: 
            In this test case when given a valid email should return true.
        """        
        self.assertTrue(Validation.validate_email("pavannakate03@gmail.com"))
        self.assertTrue(Validation.validate_email("dadamane2@yahoo.com.in"))
        self.assertTrue(Validation.validate_email("xyz.99@abc.co.in"))
        

    def test_InvalidEmail(self):
        """
        Description: 
            In this test case when given a invalid email should return false.
        """        
        self.assertFalse(Validation.validate_email("Pavan@.com"))
        self.assertFalse(Validation.validate_email("abc@.com.my"))

if __name__ == '__main__':
    unittest.main()