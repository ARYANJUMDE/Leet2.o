class Solution(object):
    def removeDuplicates(self, nums):
        # i=0
        # while i<len(nums):
        #     j=i+1
        #     while j<len(nums):
        #         if nums[i]==nums[j]:
        #             nums.pop(j)
        #         else:
        #             j=j+1
        #     i=i+1
        # return len(nums)
        
        x=list(set(nums))
        for i in range(len(x)):
            if nums.count(x[i])>1:
                while nums.count(x[i])>1:
                    nums.remove(x[i])
        return(len(nums))   




        



