class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        x=[]
        for i in range(len(capacity)):
            t=capacity[i]-rocks[i]
            if t!=0:
                x.append(t)
        x.sort()
        count=len(capacity)-len(x)
        for i in range(len(x)):
            if additionalRocks>=x[i]:
                additionalRocks=additionalRocks-x[i]
                x[i]=0
                count=count+1
            else:
                break
        
        return(count)
