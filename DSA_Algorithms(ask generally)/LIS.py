class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        1.
        ''' memo=[0]*len(nums)
        ans=0
        for i in range (len(nums)):
            max1=0
            for j in range (i+1):
                if nums[i]>nums[j] and memo[j]>max1:
                    max1=memo[j]
                else:
                    memo[i]=max1+1
            print(memo)
            ans=max(ans,memo[i])
        return ans
        3.
        n=len(nums)
        def Binary_search(self,l1,nums,n):
            l=0
            h=len(nums)-1
            while(l<h):
                mid=(l+h)>>1
                if l1[mid]==n:
                    return mid
                elif(n>l1[mid]):
                    l=mid+1
                else:
                    h=mid
        l1=[arr[0]]
        for i in range (len(nums)):
            start=nums[i]
            end=nums[n-1]
            if (start>end):
                l1.append(start)
            else:
                j=Binary_search(self,l1,nums,n)
                l1=set(j,nums)
        return len(l1)
        2>
        n=len(nums)
        dp=[0 for i in range (n)]
        for i in range(n):
            ans=1
            for j in range(i):
                if nums[j]<nums[i]:
                    ans=max(ans,dp[j]+1)
            dp[i]=ans
        return max(dp)
        '''
        n=len(nums)
        dp=[1 for i in range (n)]
        for i in range (1,n):
            for j in range (i):
                if nums[i]>nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
        
        
