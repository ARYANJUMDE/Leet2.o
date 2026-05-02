class Solution(object):
    def isCovered(self, ranges, left, right):
        x=[]
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                x.append(j)
        for i in range(left,right+1):
            if i not in x:
                return(False)
        else:
            return(True)
        