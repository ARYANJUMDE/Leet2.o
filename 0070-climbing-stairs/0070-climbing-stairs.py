class Solution(object):
    def climbStairs(self, n):
        if n==1 or n==0:
            return 1
        dp=[-1]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,len(dp)):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
        