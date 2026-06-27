class Solution(object):
    def pivotIndex(self, nums):
        # x=-1
        # for i in range(0,len(nums)):
        #     if(sum(nums[0:i])==sum(nums[i+1:len(nums)+1])):
        #         x=i
        #         break
        # if(x!=-1):
        #     return(x)
        # else:
        #     return(-1)
        for i in range(len(nums)):
            if sum(nums[:i])==sum(nums[i+1:]):
                return(i)
        else:
            return(-1)
    

        