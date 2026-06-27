class Solution(object):
    def runningSum(self, nums):
        x=[]
        for i in range(len(nums)):
            x.append(sum(nums[:i+1]))
        return(x)
        # runningsum=[]
        # t=0
        # for i in range(len(nums)):
        #     t=t+nums[i]
        #     runningsum.append(t)
        
        # return(runningsum)
        