class Solution(object):
    def getHappyString(self, n, k):
        from itertools import product
        t=['a','b','c']
        y=[]
        for i in product(t,repeat=n):
            t="".join(i)
            count=0
            for j in range(len(t)-1):
                if(t[j]!=t[j+1]):
                    count=count+1
            if(count==len(t)-1):
                y.append(t)
        if(k>len(y)):
            return("")
        else:
            
            return(y[k-1])
        