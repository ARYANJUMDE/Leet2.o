class Solution(object):
    def makeIntegerBeautiful(self, n, target):
        t=n
        sum2=0
        while t>0:
            sum2=sum2+t%10
            t=t//10
        if sum2<=target:
            return 0
        if n==target:
            return 0
        p=str(n)
        x=[]
        for i in range(len(p)):
            x.append(int(p[i]))
        sum1=sum(x)
        for i in range(len(x)-1,-1,-1):
            diff=10-x[i]
            sum1=sum1-x[i]
            x[i]=0
            if i==0:
                x.insert(0,1)  
            else:
                x[i-1]=x[i-1]+1
                j=i-1
                while j>0 and x[j]==10:
                    x[j]=0
                    x[j-1]=x[j-1]+1
                    j=j-1
            sum1=sum(x)
            if sum1<=target:
                return(int("".join(map(str,x))))-n
    
    

        