class Solution:
    def search( nums, target):
        #We devide our searching into half so searching will take less time 
        #Step1: Take the left pointer and right pointer
        #Step2:Find the middle by the formula
        #Step3:if mid index value be the target then return that index
        #Step4: Otherwise we go either left or right according to the mid value if mid index value is less then target then we left=mid+1 otherwise right=mid-1
        #Step5 if we not find then we will return -1
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+(right-left)//2)
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return -1
    nums=list(map(int,input().split()))
    target=int(input())
    print(search(nums,target))
        
