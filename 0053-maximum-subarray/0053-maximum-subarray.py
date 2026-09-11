
        
class Solution(object):
    def maxSubArray(self, nums):
        # result=[]
        # def subarray(a,i):
        #     if len(a)>0:
        #         result.append(sum(a))
        #     if i==len(nums):
        #         return
        #     else:
        #         a.append(nums[i])
        #         subarray(a,i+1)
        #         a.pop()
        #         subarray([],i+1)
        # subarray([],0)
        # return max(result)
        sum1=0
        max1=nums[0]
        for i in range(len(nums)):
            sum1=sum1+nums[i]
            if max1<sum1:
                max1=sum1
            if sum1<0:
                sum1=0
        return max1
            

        # max_sum = nums[0]
        # curr_sum = nums[0]
        
        # for i in range(1, len(nums)):
        #     # Either extend the current subarray OR start new from nums[i]
        #     curr_sum = max(nums[i], curr_sum + nums[i])
        #     max_sum = max(max_sum, curr_sum)
        
        # return max_sum

