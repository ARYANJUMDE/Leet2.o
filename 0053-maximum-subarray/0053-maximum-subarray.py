
        
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
        # sum1=0
        # max1=nums[0]
        # for i in range(len(nums)):
        #     sum1=sum1+nums[i]
        #     if max1<sum1:
        #         max1=sum1
        #     if sum1<0:
        #         sum1=0
        # return max1
        
            

        # max_sum = nums[0]
        # curr_sum = nums[0]
        
        # for i in range(1, len(nums)):
        #     # Either extend the current subarray OR start new from nums[i]
        #     curr_sum = max(nums[i], curr_sum + nums[i])
        #     max_sum = max(max_sum, curr_sum)
        
        # return max_sum


        i=0
        j=0
        sum1=0
        max_sum=float('-inf')
        while j<len(nums):
            if sum1>=0:
                sum1=sum1+nums[j]
                if sum1>max_sum:
                    max_sum=sum1
                j=j+1
            else:
                while sum1<0:
                    sum1=sum1-nums[i]
                    i=i+1
                    if sum1>max_sum:
                        max_sum=sum1
        if max_sum==0:
            if 0 in nums:
                return max_sum
        if max_sum==0:
            if 0 not in nums:
                return max(nums)
        return max_sum
        

                    
    


