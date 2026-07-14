class Solution(object):
    def arraySign(self, nums):
        x=1
        for i in range(len(nums)):
            x=x*nums[i]
        return self.signFunc(x)
    def signFunc(self,x):
        if x==0:
            return 0
        if x>0:
            return 1
        return -1

        