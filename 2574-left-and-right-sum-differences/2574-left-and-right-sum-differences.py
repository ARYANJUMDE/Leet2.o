class Solution(object):
    def leftRightDifference(self, nums):
        t=[]
        for i in range(len(nums)):
            x=sum(nums[:i])
            y=sum(nums[i+1:])
            t.append(abs(x-y))
        return(t)