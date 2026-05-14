class Solution(object):
    def isGood(self, nums):
        z=max(nums)
        if(nums.count(z)==2):
            for i in range(1,z):
                if i not in nums or nums.count(i)>1:
                    return(False)
            else:
                return(True)
        else:
            return(False)
    
    
