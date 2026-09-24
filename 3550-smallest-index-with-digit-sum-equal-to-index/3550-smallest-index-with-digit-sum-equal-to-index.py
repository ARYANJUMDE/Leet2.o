class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            sum1=0
            while nums[i]>0:
                sum1=sum1+nums[i]%10
                nums[i]=nums[i]//10
            if sum1==i:
                return i
        return -1
