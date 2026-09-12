class Solution(object):
    def longestOnes(self, nums, k):
        # x=[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)+1):
        #         if nums[i:j].count(0)<=k:
        #             x.append(len(nums[i:j]))
        # if len(x)==0:
        #     return 0
        # return(max(x))
        l=0
        r=0
        max_len=0
        final_len=0
        while r<len(nums):
            if k>0:
                max_len=max_len+1
                if nums[r]==0:
                    k=k-1
            else:
                if nums[r]==1:
                    max_len=max_len+1
                else:
                    while k==0:
                        if nums[l]==0:
                            k=k+1
                        l=l+1
                        max_len=max_len-1
                    max_len=max_len+1
                    k=k-1
            if max_len>final_len:
                final_len=max_len
            r=r+1
        return final_len
                
                        
                    