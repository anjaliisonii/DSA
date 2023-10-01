#CheckPassword
'''Q.2 Write a function CheckPassword(str) which will
accept the string as an argument or parameter and validates
the password. It will return 1 if the conditions are satisfied
else it’ll return 0?'''
#Rule
'''The password is valid if it satisfies the below conditions:

It should contain at least 4 characters.
At least 1 numeric digit should be present.
1 Capital letter should be there.
Password should not contain space or slash.
The starting character should not be a number.'''
def validate_Password(pswd):
    if len(pswd)<=3:
        return 0
    digit_count=0
    upper=0
    for i in range (len(pswd)):
        if i==0 and pswd[i].isdigit():
            return 0
        if pswd[i]==" " or pswd[i]=="/" :
            return 0
        if pswd[i].isupper():
            upper+=1
        if pswd[i].isdigit():
            digit_count+=1
    if upper==1 and digit_count>=1:
        return 1
    else:
        return 0
str1=input()
print(validate_Password(str1))





    
            
        
