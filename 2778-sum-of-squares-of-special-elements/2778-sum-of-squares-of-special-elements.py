class Solution(object):
    def sumOfSquares(self, nums):
        sum1=0
        x=len(nums)
        for i in range(1,len(nums)+1):
            if x%i==0:
                sum1=sum1+nums[i-1]*nums[i-1]
        return sum1

        