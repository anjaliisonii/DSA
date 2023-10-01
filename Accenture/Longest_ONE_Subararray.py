#longest Subarray having count of 1s one more than count0s
'''Given an array of size n containing 0’s and 1’s only.
The problem is to find the length of the longest
subarray having count of 1’s one more than count of 0’s. 
Input : arr = {0, 1, 1, 0, 0, 1}
Output : 5
From index 1 to 5.

Input : arr[] = {1, 0, 0, 1, 0}
Output : 1'''
def longest_1_subarray(arr):
    dict1={}
    sum1=0
    max_len=0
    for i in range (len(arr)):
        if arr[i]==0:
            sum1-=1
        elif arr[i]==1:
            sum1+=1
        if sum1==1:
            max_len=i+1
        elif sum1 not in dict1:
            dict1[sum1]=i
        if sum1-1 in dict1:
            if (max_len < (i - dict1[sum1 - 1])):
                max_len = i - dict1[sum1 - 1]
    return max_len
nums=list(map(int,input().split()))
print(longest_1_subarray(nums))
    
