class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        count=0
        x=money
        for i in range(len(prices)):
            t=money-prices[i]
            if t>=0 and count!=2:
                money=money-prices[i]
                count=count+1
            else:
                break
        if count==2 and money>=0:
            return money
        return x
