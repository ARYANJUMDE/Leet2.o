class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        maxlen1=float('-inf')
        maxlen2=float('-inf')
        i=0
        j=0
        currlen1=1
        currlen2=1
        while i<len(nums)-1:
            if nums[i]<nums[i+1]:
                currlen1=currlen1+1
            else:
                currlen1=1
            if currlen1>maxlen1:
                maxlen1=currlen1
            i=i+1
        
        while j<len(nums)-1:
            if nums[j]>nums[j+1]:
                currlen2=currlen2+1
            else:
                currlen2=1
            if currlen2>maxlen2:
                maxlen2=currlen2
            j=j+1
        return max(maxlen1,maxlen2)
        

            





        