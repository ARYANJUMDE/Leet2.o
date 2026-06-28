class Solution(object):
    def sortedSquares(self, nums):
        # x=[]
        # for num in nums:
        #     x.append(num*num)
        # x.sort()
        # return x
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums.sort()
        return(nums)

        