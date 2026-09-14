class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        count1=0
        sum1=0
        r=0
        l=0
        while r<len(nums):
            sum1=sum1+nums[r]
            if sum1>goal:
                while sum1>goal:
                    sum1=sum1-nums[l]
                    l=l+1
            count1=count1+(r-l+1)
            r=r+1
        sum1=0
        count2=0
        r=0
        l=0
        if goal==0:
            return count1
        while r<len(nums):
            sum1=sum1+nums[r]
            if sum1>goal-1:
                while sum1>goal-1:
                    sum1=sum1-nums[l]
                    l=l+1
            count2=count2+(r-l+1)
            r=r+1
        return abs(count2-count1)
        
        