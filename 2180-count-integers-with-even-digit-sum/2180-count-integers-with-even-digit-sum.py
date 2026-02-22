class Solution(object):
    def countEven(self, num):
        x=[]
        y=[]
        for i in range(1,num+1):
            x.append(str(i))
        for i in range(len(x)):
            s=0
            for j in range(len(x[i])):
                s=s+int(x[i][j])
            if(s%2==0):
                y.append(s)
        
        return(len(y))

    

        