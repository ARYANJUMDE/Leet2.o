class Solution(object):
    def maximizeSum(self, nums, k):
        s=0
        for i in range(k):
            s=s+max(nums)
            t=max(nums)
            nums.append(max(nums)+1)
            nums.remove(t)
        return(s)

        