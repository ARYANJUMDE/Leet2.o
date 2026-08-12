class Solution(object):
    def fib(self, n):
        # if(n==0 or n==1):
        #     return n
        # l=[0,1]
        # for i in range(2,n):
        #     l.append(l[i-1]+l[i-2])
        
        # return l[len(l)-1]+l[len(l)-2]
        if n==0:
            return 0
        if n==1:
            return 1
        dp=[-1]*(n+1)
        dp[0]=0
        dp[1]=1

        for i in range(2,len(dp)):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]



S=Solution()
S.fib(2)
        
        