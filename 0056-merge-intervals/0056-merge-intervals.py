class Solution(object):
    def merge(self, intervals):
        x=sorted(intervals,key=lambda t:t[0])
        y=[x[0]]
        for i in range(1,len(x)):
            if(y[-1][1]>=x[i][0]):
                y[-1][1]=max(y[-1][1],x[i][1])
            else:
                y.append(x[i])
        
        
        return(y)


        