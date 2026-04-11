class Solution(object):
    def finalPrices(self, prices):
        answer=[]
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    
                    answer.append(prices[i]-prices[j])
                    break
            else:
                answer.append(prices[i])
        return(answer)