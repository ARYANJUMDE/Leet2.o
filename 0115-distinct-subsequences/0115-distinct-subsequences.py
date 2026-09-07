class Solution(object):
    def numDistinct(self, s, t):
        # result=[0]
        # def solve(i,y):
        #     if len(y)>len(t):
        #         return
        #     if i==len(s):
        #         if y==t:
        #             result[0]=result[0]+1
        #         return
        #     else:
        #         y=y+s[i]
        #         solve(i+1,y)
        #         y=y[:-1]
        #         solve(i+1,y)
        # solve(0,"")
        # return result[0]

        dp=[[-1]*len(t) for i in range(len(s))]
        def solve(i,j,dp):
            if j<0:
                return 1
            if i<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if t[j]==s[i]:
                dp[i][j]=solve(i-1,j-1,dp)+solve(i-1,j,dp)
            if t[j]!=s[i]:
                dp[i][j]=solve(i-1,j,dp)
            return dp[i][j]
        p=solve(len(s)-1,len(t)-1,dp)
        return(p)

            



        