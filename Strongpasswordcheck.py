def passwordCheck(password):
    if lowercaseRegex.search(password) == None:
        print('You need lowercase letters')
    elif uppercaseRegex.search(password) == None:
        print('You need uppercase letters')
    elif numberRegex.search(password) == None:
        print('You need numbers')
    elif longRegex.search(password) == None:
        print('You need a longer password')
    else:
        print('Your password is strong enough')
        
import re
lowercaseRegex = re.compile(r'[a-z]')
uppercaseRegex = re.compile(r'[A-Z]')
numberRegex = re.compile(r'[0-9]')
longRegex = re.compile(r'(.){8,50}')
print('What is your password?') 
password = input()  
passwordCheck(password)
cat = longRegex.search('doggo')
