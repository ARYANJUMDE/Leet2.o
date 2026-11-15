class Solution(object):
    def minPairSum(self, nums):
        nums.sort()
        max_sum=float('-inf')
        for i in range(len(nums)//2):
            curr_sum=nums[i]+nums[len(nums)-i-1]
            if max_sum<curr_sum:
                max_sum=curr_sum
        return max_sum
        