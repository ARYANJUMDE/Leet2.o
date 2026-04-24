class Solution(object):
    def differenceOfSum(self, nums):
        t=sum(nums)
        y=0
        for i in range(len(nums)):
            while nums[i]>0:
                x=nums[i]%10
                y=y+x
                nums[i]=nums[i]//10
        
        
        return(abs(t-y))
        