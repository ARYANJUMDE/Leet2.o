class Solution(object):
    def removeElement(self, nums, val):
        # i=len(nums)-1
        # while(i>=0):
        #     if(nums[i]==val):
        #         nums.pop(i)
        #     i=i-1
        # return(len(nums))
        # return(nums)
        x=list(set(nums))
        for i in range(len(x)):
            if x[i]==val:
                while nums.count(x[i])>0:
                    nums.remove(x[i])
        return(len(nums))


        