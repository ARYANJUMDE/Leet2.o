class Solution(object):
    def groupThePeople(self, groupSizes):
        x=list(set(groupSizes))
        result=[]
        for i in range(len(x)):
            t=[]
            for j in range(len(groupSizes)):
                if groupSizes[j]==x[i]:
                    t.append(j)
            if len(t)==x[i]:
                result.append(t)
            else:
                o=[]
                for k in range(0,len(t)):
                    if len(o)<x[i]:
                        o.append(t[k])
                    else:
                        result.append(o)
                        o=[]
                        o.append(t[k])
                if len(o)>0:
                    result.append(o)
        return result
            
        