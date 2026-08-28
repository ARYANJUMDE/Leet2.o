class Solution(object):
    def rob(self, nums):
        # dp=[-1]*len(nums)
        # def robbing(i):
        #     if i>=len(nums):
        #         return 0
        #     if dp[i]!=-1:
        #         return dp[i]
        #     take=nums[i]+robbing(i+2)
        #     skip=robbing(i+1)
        #     dp[i]=max(take,skip)
        #     return dp[i]
        # return robbing(0)
        dp=[-1]*len(nums)
        def robbing(i):
            if i>=len(nums):
                return 0
            if dp[i]!=-1:
                return dp[i]
            else:
                take=nums[i]+robbing(i+2)
                skip=robbing(i+1)
                dp[i]=max(take,skip)
                return dp[i]
        return robbing(0)
        # # dp=[-1]*len(nums)
        # for i in range(len(nums)):
        
        # Normal recusion code
        # x=[]
        # def robbing(sum1,i):
        #     if i>=len(nums):
        #         x.append(sum1)
        #         return
        #     else:
        #         sum1=sum1+nums[i]
        #         robbing(sum1,i+2)
        #         sum1=sum1-nums[i]
        #         robbing(sum1,i+1)
        # t=robbing(0,0)
        # return (max(x))    

        # prev1 = 0
        # prev2 = 0
        
        # for num in nums:
        #     temp = max(prev1, prev2 + num)
        #     prev2 = prev1
        #     prev1 = temp
        
        # return prev1