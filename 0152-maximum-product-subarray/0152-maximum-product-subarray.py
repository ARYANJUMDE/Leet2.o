import math
class Solution(object):
    def maxProduct(self, nums):
        #x=[]
        #maxi = maximum product till current index
        #mini = minimum product till current index
        #We keep minimum also because:negative × negative = positive
        # maxi=nums[0]
        # mini=nums[0]
        # ans=nums[0]

        # for i in range(1,len(nums)):

        #     #Needed because maxi changes before calculating mini.
        #     temp=maxi
        #     #At every element, 3 possibilities:
        #     #Start new subarray Extend previous maximum product or Extend previous minimum product
        #     maxi=max(nums[i],maxi*nums[i],mini*nums[i])
        #     mini=min(nums[i],temp*nums[i],mini*nums[i])

        #     #Store global maximum.

        #     ans=max(ans,maxi)

        # return(ans)
        max_prod=float('-inf')
        prefix=1
        suffix=1
        for i in range(len(nums)):
            prefix=prefix*nums[i]
            suffix=suffix*nums[len(nums)-1-i]
            if max_prod<prefix:
                max_prod=prefix
            if max_prod<suffix:
                max_prod=suffix
            if nums[i]==0:
                prefix=1
            if nums[len(nums)-i-1]==0:
                suffix=1
        if max_prod==float('-inf'):
            return min(nums)
        if max_prod<0 and 0 not in nums :
            return(max_prod)
        elif max_prod<0 and 0 in nums:
            return(0)
        else:
            return(max_prod)
    

        