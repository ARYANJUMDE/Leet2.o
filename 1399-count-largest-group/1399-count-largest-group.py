class Solution(object):
    def countLargestGroup(self, n):
        x=[]
        for i in range(1,n+1):
            s=0
            t=str(i)
            for ch in t:
                s=s+int(ch)
            x.append(s)
        r=list(set(x))
        y=x.count(x[0])
        count=0

        for num in r:
            if x.count(num)>y:
                y=x.count(num)
        
        for num in r:
            if x.count(num)==y:
                count=count+1
        return(count)
        