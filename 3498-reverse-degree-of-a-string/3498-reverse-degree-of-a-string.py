class Solution(object):
    def reverseDegree(self, s):
        x=[]
        y=[]
        z=[]
        for i in range(26,0,-1):
            x.append(i)
        for ch in range(97,123):
            y.append(chr(ch))
        cost=0
        for i in range(len(x)):
            z.append((y[i],x[i]))
        
        for i in range(len(s)):
            for j in range(len(z)):
                if s[i]==z[j][0]:
                    
                    cost=cost+(i+1)*z[j][1]

        
        return(cost)

        