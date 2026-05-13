class Solution(object):
    def sumZero(self, n):
        if n==1:
            return([0])
        else:
            x=[]
            if n%2==0:
                for i in range(1,(n/2)+1):
                    x.append(i)
                for j in range(1,(n/2)+1):
                    x.append(-j)
            else:
                
                for i in range(0,(n//2)+1):
                    x.append(i)
                for j in range(1,(n//2)+1):
                    
                    x.append(-j)
                
                
        return(x)
        

        