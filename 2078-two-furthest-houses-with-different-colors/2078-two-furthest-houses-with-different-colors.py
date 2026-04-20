class Solution(object):
    def maxDistance(self, colors):
        x=[]
        for i in range(len(colors)):
            for j in range(i+1,len(colors)):
                if colors[i]!=colors[j]:
                    x.append(abs(i-j))
        return(max(x))
        