class Solution(object):
    def minElement(self, nums):
        x=[]
        for i in range(len(nums)):
            s=0
            while nums[i]>0:
                t=nums[i]%10
                s=s+t
                nums[i]=nums[i]//10
            x.append(s)
        
        return(min(x))
        
    

        