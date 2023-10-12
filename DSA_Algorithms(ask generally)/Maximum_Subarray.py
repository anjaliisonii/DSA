class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max1=max(nums)
        curr=0
        for i in nums:
            curr+=i
            if(curr>max1):
                max1=curr
            elif(curr<0):
                curr=0
        return max1
        
