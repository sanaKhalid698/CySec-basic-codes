'''Create a program that checks the strength of a password based on predefined criteria 
(length, use of uppercase letters, lowercase letters, digits, and special characters).
Analyze the password based on various criteria:
Length: Minimum length (e.g., 8 characters).
Complexity: Check for the presence of:
Uppercase letters (A-Z)
Lowercase letters (a-z)
Numbers (0-9)
Special characters (e.g., !@#$%^&*)
'''

def password_checker(password_input:str):
    length: bool= (len(password_input)>=8)
    has_Uppercase: bool= any(char.isupper() for char in password_input)
    has_Lowercase:bool=any(char.islower() for char in password_input)
    has_numbers:bool= any(char.isdigit()for char in password_input)
    has_specialchar:bool=any(char.isalnum()for char in password_input)
    criteria: int =sum(length+has_Lowercase+has_numbers+has_specialchar+has_Uppercase)
    if criteria==5:
        return "strong"
    elif criteria ==4:
        return "moderate"
    else:
        return "weak"

if __name__=="__main__":
    password_input: str =input("Enter the password:")
    check: str = password_checker(password_input)
    print(check)
