class Solution(object):
    def maximumWealth(self, accounts):
        t=[]
        for i in range(len(accounts)):
            t.append(sum(accounts[i]))
        return(max(t))
        