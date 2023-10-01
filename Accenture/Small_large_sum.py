#SMALL Large Sum
'''Q.1 Write a function SmallLargeSum(array) which accepts
the array as an argument or parameter, that performs
the addition of the second largest element from the even location
with the second largest element from an odd location?
Rule # All the array elements are unique.
If the length of the array is 3 or less than 3, then return 0.
If Array is empty then return zero.'''
def small_Large_sum(nums):
    if len(nums)<=3:
        return 0
    even=[]
    odd=[]
    for i in range (len(nums)):
        if i%2==0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    even.sort()
    odd.sort()
    return even[1]+odd[1]
nums=list(map(int,input().split()))
print(small_Large_sum(nums))
            
