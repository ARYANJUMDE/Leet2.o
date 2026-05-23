class Solution(object):
    def isMonotonic(self, nums):
        if nums==sorted(nums):
            return(True)
        elif nums==sorted(nums,reverse=True):
            return(True)
        else:
            return(False)

        