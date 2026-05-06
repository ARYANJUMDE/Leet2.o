class Solution(object):
    def kthDistinct(self, arr, k):
        x=[]
        for ch in arr:
            if arr.count(ch)==1:
                x.append(ch)
        if(len(x)<k):
            return("")
        else:
            return(x[k-1])
