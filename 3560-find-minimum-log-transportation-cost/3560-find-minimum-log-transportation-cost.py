class Solution(object):
    def minCuttingCost(self, n, m, k):
        cost=0
        if m<=k:
            cost=0
        else:
            diff=m-k
            cost=cost+diff*k
        if n<=k:
            cost=cost+0
        else:
            diff=n-k
            cost=cost+diff*k
        return(cost)