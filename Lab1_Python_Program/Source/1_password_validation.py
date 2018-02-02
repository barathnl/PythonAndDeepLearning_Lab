import sys
import re

print("Please enter your new password : ")
password = sys.stdin.readline()

'''
To check whether length of password in range of 6 and 16
'''
if((len(password))>=6 and(len(password))<=16):
    print("Password is in range between 6 and 16")
else:
    print("Password is NOT in range between 6 and 16")

'''
To check whether password contain number using regular expression
'''
if(re.search("[0-9]",password)):
    print("Password contain atleast one number")
else:
    print("Password does NOT contain atleast one number")


'''
To check whether password contain atleast Special character using regular expression
'''
if(re.search("[$@*!]",password)):
    print("Password contain atleast one special character")
else:
    print("Password does NOT contain atleast one special character")

'''
To check whether password contain atleat one lower and upper case using regular expression
'''
if((re.search("[a-z]",password)) and (re.search("[A-Z]",password))):
    print("Password contain atleast one lower case and upper case letter")
else:
    print("Password does NOT contain atleast one lower or upper case letter")