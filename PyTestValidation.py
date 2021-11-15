'''
@Author: Pavan Nakate
@Date: 2021-11-14 11:43
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : User-Registration-Program  
'''
from InfoVAlidation import Validation
import pytest
import json

with open('ValidData.json') as f:
    data = json.load(f)
    
    def test_validFirstName():
        """
        Description: 
            In this test case when given a valid first name should return true.
        """ 
    
        for user in data:
            f_name = user['firstName']
            assert Validation.validate_first_name(f_name) == True

    def test_validLastName():
        """
        Description: 
            In this test case when given a valid last name should return true.
        """ 

        for user in data:
            l_name = user['lastName']
            assert Validation.validate_last_name(l_name) == True

    def test_validMobileNumber():
        """
        Description: 
            In this test case when given a valid mobile number should return true.
        """ 

        for user in data:
            phone_no = user['mobile']
            assert Validation.validate_mobile(phone_no) == True

    def test_validPassword():
        """
        Description: 
            In this test case when given a valid password should return true.
        """ 

        for user in data:
            passcode = user['password']
            assert Validation.validate_password(passcode) == True

    def test_validEmail():
        """
        Description: 
            In this test case when given a valid email should return true.
        """ 

        for user in data:
            mail = user['email']
            assert Validation.validate_email(mail) == True


with open('InvalidData.json') as in_f:
    invalid_data = json.load(in_f)

    def test_invalidFirstName():
        """
        Description: 
            In this test case when given a invalid first name should return false.
        """ 

        for user in invalid_data:
            f_name = user['firstName']
            assert Validation.validate_first_name(f_name) == False

    def test_invalidLastName():
        """
        Description: 
            In this test case when given a invalid last name should return false.
        """ 

        for user in invalid_data:
            l_name = user['lastName']
            assert Validation.validate_last_name(l_name) == False

    def test_invalidMobileNumber():
        """
        Description: 
            In this test case when given a invalid mobile number should return false.
        """ 

        for user in invalid_data:
            phone_no = user['mobile']
            assert Validation.validate_mobile(phone_no) == False

    def test_invalidPassword():
        """
        Description: 
            In this test case when given a invalid password should return false.
        """
        for user in invalid_data:
            passcode = user['password']
            assert Validation.validate_password(passcode) == False

    def test_invalidEmail():
        """
        Description: 
            In this test case when given a invalid email should return false.
        """ 

        for user in invalid_data:
            mail = user['email']
            assert Validation.validate_email(mail) == False