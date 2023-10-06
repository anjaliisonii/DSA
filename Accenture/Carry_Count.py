#Problem Statement
'''A carry is a digit that is transferred to left if sum of digits exceeds 9
while adding two numbers from right-to-left one digit at a time
You are required to implement the following function.
Int NumberOfCarries(int num1 , int num2);
The functions accepts two numbers ‘num1’ and ‘num2’ as its arguments.
You are required to calculate and return  the total number of carries generated
while adding digits of two numbers ‘num1’ and ‘ num2’.
Assumption: num1, num2>=0

Example:
Input
  Num 1: 451
  Num 2: 349
Output
  2'''
num1=int(input())
num2=int(input())
sum1=0
carry=0
count=0
l1=[]
while num1 and num2:
    a=num1%10
    b=num2%10
    sum1=carry+a+b
    s=str(sum1)
    l1.append(s[-1])
    if sum1>9:
        carry=1
        count+=1
    else:
        carry=0
    num1//=10
    num2//=10
while num1:
    a=num1%10
    sum1=carry+a
    s=str(sum1)
    l1.append(s[-1])
    if sum1>9:
        carry=1
        count+=1
    else:
        carry=0
    num1//=10
while num2:
    b=num2%10
    sum1=carry+b
    s=str(sum1)
    l1.append(s[-1])
    if sum1>9:
        carry=1
        count+=1
    else:
        carry=0
    num2//=10
    
ans="".join(l1)
print(ans[::-1])
print(count)
    
