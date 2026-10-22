class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        nums.sort()
        right=0
        left=0
        max_len=float('-inf')
        curr_len=1
        while right<len(nums)-1:
            if nums[right+1]==nums[right]+1:
                curr_len=curr_len+1
            elif nums[right+1]==nums[right]:
                pass
            else:
                while left!=right+1:
                    left=left+1
                    curr_len=curr_len-1
                curr_len=1
            if curr_len>max_len:
                max_len=curr_len
            right=right+1
            
        return(max_len)

        