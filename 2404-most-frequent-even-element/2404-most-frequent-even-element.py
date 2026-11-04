class Solution(object):
    def mostFrequentEven(self, nums):
        x={}
        for i in range(len(nums)):
            if nums[i]%2==0:
                if nums[i] not in x:
                    x[nums[i]]=1
                else:
                    x[nums[i]]=x[nums[i]]+1
        if len(x)>0:
            x=sorted(x.items(),key=lambda x:(x[1],-x[0]),reverse=True)
            return x[0][0]
        return -1
        
