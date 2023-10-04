str1="Move-Hyphens-to-Front"
n=len(str1)
ans=""
count=0
for i in range (n):
    if str1[i]=='-':
        count+=1
    else:
        ans+=str1[i]
        
while count:
    ans='-'+ans
    count-=1
print(ans)
