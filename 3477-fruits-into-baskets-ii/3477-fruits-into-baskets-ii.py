class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        x=[]
        for i in range(len(fruits)):
            for j in range(len(baskets)):
                if(baskets[j]>=fruits[i]):
                    x.append(fruits[i])
                    baskets.pop(j)
                    break
        
        return(len(fruits)-len(x))

        