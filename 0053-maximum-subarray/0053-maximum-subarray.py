class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        l=0
        r=0
        sum1=0
        max_sum=float('-inf')
        while r<len(nums):
            sum1=sum1+nums[r]
            if sum1<0:
                while sum1<0:
                    sum1=sum1-nums[l]
                    l=l+1
            if sum1>max_sum:
                max_sum=sum1
            r=r+1
        if max_sum==0:
            if 0 not in nums:
                return max(nums)
        return(max_sum)
    
        



        