'''
@Author: Pavan Nakate
@Date: 2021-11-14 11:43
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : User-Registration-Program  
'''
from InfoVAlidation import Validation
import pytest

def test_validFirstName():
    """
    Description: 
        In this test case when given a valid first name should return true.
    """ 
    
    validFirstName = ["Pavan","Jay"]
    
    for names in validFirstName:
        assert Validation.validate_first_name(names) == True

def test_invalidFirstName():
    """
    Description: 
        In this test case when given a invalid first name should return false.
    """ 

    invalidFirstName = ["rahul", "anna", "hari23", "s@minum" ]

    for names in invalidFirstName:
        assert Validation.validate_first_name(names) == False

def test_validLastName():
    """
    Description: 
        In this test case when given a valid last name should return true.
    """ 

    validLastName = ["Nakate", "Mane"]

    for names in validLastName:
        assert Validation.validate_last_name(names) == True


def test_invalidLastName():
    """
    Description: 
        In this test case when given a invalid last name should return false.
    """ 

    invalidLastName = ["rathod", "Shinde3", "xyz$"]

    for names in invalidLastName:
        assert Validation.validate_last_name(names) == False