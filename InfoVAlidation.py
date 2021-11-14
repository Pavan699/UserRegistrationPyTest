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

if __name__ == "__main__":
    print(Validation.validate_first_name("Pavan"))
    print(Validation.validate_first_name("Nakate"))