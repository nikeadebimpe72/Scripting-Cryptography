#1/usr/bin/env python3

passwords =[
"W4$acxyH7BtQiU3er",
"Zk7i$F8uo#Aq",
"L#1npOdATe2rjy",
"vE@XsLwzKmy",
"cBa6Hg7@uY3WjR",
"QpiTcS7Ozlk2"
]

def check_password(passwords):
   
        if len(passwords)  < 6 or len(passwords) > 16:
            return f"{passwords} must be between 6 to 16" 
        
        if  not any(char.isupper() for char in passwords):
            return f"{passwords} must contain both upper case"
        
        if  not any(char.islower() for char in passwords): 
            return f"{passwords} must contain  lower case"
        
        if  not any(char.isdigit() for char in passwords):
            return f"{passwords} must be contain a number"
        
        if not any(char in "@#$" for char in passwords):
            return f"{passwords} must contain special character"
            
        return f"{passwords} is valid"
for p in passwords:
    print(check_password(p))

        
   
        