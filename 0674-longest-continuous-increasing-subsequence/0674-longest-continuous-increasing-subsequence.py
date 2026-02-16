class Solution(object):
    def findLengthOfLCIS(self, nums):
        # count=0
        # for i in range(len(nums)-1):
        #     if(nums[i]<nums[i+1]):
        #         count=count+1
        # if(count==0):
        #     return(1)
        # else:
        #     return(count)
        max_len=1
        curr_len=1
        
        for i in range(len(nums)-1):
            if(nums[i]<nums[i+1]):
                curr_len=curr_len+1
                
                max_len=max(max_len,curr_len)
            else:
                curr_len=1
        return(max_len)
        