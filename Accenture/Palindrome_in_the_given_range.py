def reverse(n,rev):
    while n:
        d=n%10
        rev=rev*10+d
        n//=10
    return rev
def check_palindrome(a,b):
    l1=[]
    for i in range (a,b):
        rev=0
        n=i
        ans=reverse(n,rev)
        if i==ans:
            l1.append(i)
    return l1
            
a,b=map(int,input().split())
print(check_palindrome(a,b))
