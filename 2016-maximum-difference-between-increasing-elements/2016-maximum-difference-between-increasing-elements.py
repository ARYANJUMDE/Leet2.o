class Solution(object):
    def maximumDifference(self, nums):
        x=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]<nums[j]):
                    x.append(nums[j]-nums[i])
        if(len(x)==0):
            return(-1)
        else:
            return(max(x))
        