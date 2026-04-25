class Solution(object):
    def canJump(self, nums):
        reach=0
        #This stores the farthest index you can reach so far
        #Initially, you're at index 0, so reach = 0
        for i in range(len(nums)):
            #If current index i is greater than what you can reach,
            #it means:
            #you can’t even get to this position
            if i>reach:
                return(False)
            else:
                reach=max(reach,i+nums[i])
        else:
            return(True)