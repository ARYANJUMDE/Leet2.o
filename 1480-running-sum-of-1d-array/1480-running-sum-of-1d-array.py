class Solution(object):
    def runningSum(self, nums):
        runningsum=[]
        t=0
        for i in range(len(nums)):
            t=t+nums[i]
            runningsum.append(t)
        
        return(runningsum)
        