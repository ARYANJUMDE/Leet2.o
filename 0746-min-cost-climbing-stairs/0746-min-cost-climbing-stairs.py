class Solution(object):
    def minCostClimbingStairs(self, cost):
        def climb(t,dp):
            if t<=1:
                return 0
            if dp[t]!=-1:
                return dp[t]
            dp[t]= min(climb(t-1,dp)+cost[t-1],climb(t-2,dp)+cost[t-2])
            return dp[t]
        o=climb(len(cost),[-1]*(len(cost)+1))
        return(o)

        