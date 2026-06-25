class Solution(object):
    def uniqueOccurrences(self, arr):
        x=list(set(arr))
        y=[]
        for i in range(len(x)):
            y.append(arr.count(x[i]))
        if len(set(y))==len(y):
            return(True)
        else:
            return(False)
        