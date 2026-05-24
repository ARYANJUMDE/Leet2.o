class Solution(object):
    def getMaximumGenerated(self, n):
        if n==0:
            return 0
        nums=[0,1]
        while len(nums)<n+1:
            for i in range(1,n+1):
                if 2*i%2==0 and len(nums)<n+1:
                    nums.append(nums[i])
                
                if (2*i+1)%2!=0 and len(nums)<n+1:
                    nums.append(nums[i]+nums[i+1])
        return(max(nums))
        

        