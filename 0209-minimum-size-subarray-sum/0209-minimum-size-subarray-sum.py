class Solution(object):
    def minSubArrayLen(self, target, nums):
        sum1=0
        x=[]
        result=[]
        for i in range(len(nums)):
            sum1=sum1+nums[i]
            x.append(nums[i])
            if sum1>=target:
                while sum1>=target:
                    result.append(len(x))
                    sum1=sum1-x[0]
                    x.pop(0)
        if len(result)==0:
            return 0
        return min(result)



        