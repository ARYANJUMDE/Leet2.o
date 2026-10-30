class Solution(object):
    def sumOfUnique(self, nums):
        x={}
        for i in range(len(nums)):
            if nums[i] not in x:
                x[nums[i]]=1
            else:
                x[nums[i]]=x[nums[i]]+1
        x=list(sorted(x.items(),key=lambda x:x[1]))
        t=0
        for i in range(len(x)):
            if x[i][1]==1:
                t=t+x[i][0]
            else:
                break
        return t

        


