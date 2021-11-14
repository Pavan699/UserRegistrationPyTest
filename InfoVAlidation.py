'''
@Author: Pavan Nakate
@Date: 2021-11-13 10:22
@Last Modified by: Pavan Nakate
@Last Modified time: None
@Title : User-Registration-Program  
'''
print("Welcome to User Registration Program")

import re

class Validation():
    """
    Description:
        This Class having Functions to validate the user details
    """  

    def validate_first_name(firstName):
        """
        Description:
            This function is to validate first name.
            Condition: Name should start with Capital letter and should have min 3 letters.
        Args:
            firstName: First name to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^[A-Z]{1}[a-z]{2,}$", firstName))

        except Exception as e:
            print("Exception",e)

    def validate_last_name(lastName):
        """
        Description:
            This function is to validate last name.
            Condition: Last name should start with Capital letter and should have min 2 letters.
        Args:
            lastName: Last name to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^[A-Z]{1}[a-z]{1,}$", lastName))

        except Exception as e:
            print("Exception",e)

    def validate_mobile(mobile):
        """
        Description:
            This function is to validate mobile number.
            Condition: Mobile number should start with country code 91
            and followed by space and 10 digits.
        Args:
            mobile: Mobile number to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^(91)\\s[6-9]{1}[0-9]{9}$", mobile))

        except Exception as e:
            print("Exception",e)

    def validate_password(password):
        """
        Description:
            This function is to validate password.
            Password contain minimum 8 letters.
            Password contain one upper and lower case.
            Password contain one numeric and special character.
        Args:
            password: Password to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^(?=.*\d)(?=.*[@#$%&])(?=.*[a-z])(?=.*[A-Z]).{8,}$", password))

        except Exception as e:
            print("Exception",e)

    def validate_email(email):
        """
        Description:
            This function is to validate email.
        Args:
            email: email to validate
        Returns:
            boolean result
        """        
        try:
            return bool(re.match("^[0-9A-Za-z]+(([._+-]{0,1})[0-9A-Za-z]+)*@[0-9A-Za-z]+.[a-z]{2,4}.([a-z]{2,3})*$", email))

        except Exception as e:
            print("Exception",e)

if __name__ == "__main__":
    print(Validation.validate_first_name("Pavan"))
    print(Validation.validate_last_name("Nakate"))
    print(Validation.validate_mobile("91 9960748875"))
    print(Validation.validate_password("Pavan@699"))
    print(Validation.validate_email("pavannakate03@gmail.com"))