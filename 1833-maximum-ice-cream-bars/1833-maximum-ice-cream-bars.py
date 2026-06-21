class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        count=0
        for i in range(len(costs)):
            if costs[i]<=coins:
                count=count+1
                coins=coins-costs[i]
            else:
                break   
        return(count)

        