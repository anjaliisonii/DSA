class Solution:
    def searchInsert(nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return left
    target=int(input())
    nums=list(map(int,input().split()))
    print(searchInsert(nums,target))
        

