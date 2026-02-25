class Solution(object):
    def repeatedNTimes(self, nums):
        x=[]
        for num in nums:
            if num not in x:
                x.append(num)
        for num in x:
            if 2*nums.count(num)==len(nums):
                return(num)
    

        