class Solution(object):
     def twoSum(self, nums, target):
#         for i in range(0,len(nums)-1):
#             for j in range(i+1,len(nums)):
#                 if(nums[i]+nums[j]==target):
#                     return [i,j]
# S=Solution()
# S.twoSum([2,7,11,15],9)
            # for i in range(len(nums)-1):
            #     for j in range(i+1,len(nums)):
            #         if nums[i]+nums[j]==target:
            #             return([i,j])

            t={}
            for i in range(len(nums)):
                if i not in t:
                    t[i]=nums[i]
            for i in (t):
                diff=target-t[i]
                for j in range(i+1,len(t)):
                    if t[j]==diff:
                        return([i,j])
    

