class Solution(object):
    def firstStableIndex(self, nums, k):
        min1=[0]*len(nums)
        min1[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            min1[i]=min(nums[i],min1[i+1])
        max1=nums[0]
        for i in range(len(nums)):
            if max1<nums[i]:
                max1=nums[i]
            if max1-min1[i]<=k:
                return(i)
        return -1
        
