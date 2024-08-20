import sys
def emailvalidation(email):
    if len(email) < 10 :
        print("email is too short")
        sys.exit()
    elif "@" not in email or "." not in email:
        print("email must contains '@' and '.'") 
        sys.exit()
    elif email.count("@") > 1 :
        print(f"email contains only one '@' . Here '@'  symbol {email.count("@")} times occured")
        sys.exit()
    splited_email = email.split("@")
    user_name = splited_email[0]
    last_position = splited_email[1]
    if user_name.isalnum() == False:
        print("User name does not allow special characters")
        sys.exit()
    split_last_position = last_position.split(".")
    domain = split_last_position[0]
    extention = split_last_position[1] 
    if len(domain) < 3:
        print("domain name atleast contains 3 characters")
        sys.exit()
    elif len(extention) < 3:
        print("check the extention properly")
        sys.exit()
    print(f"You Email Id {email} is Valid")
email = input("Enter your Email Id : ")
emailvalidation(email)


'''
OUTPUT:-

Enter your Email Id : cognifyz@gmail.com
You Email Id cognifyz@gmail.com is Valid

Enter your Email Id : cognifyz@gmail    
email must contains '@' and '.'
'''