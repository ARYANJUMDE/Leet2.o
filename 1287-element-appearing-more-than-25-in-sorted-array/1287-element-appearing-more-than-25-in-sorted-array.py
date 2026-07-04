class Solution(object):
    def findSpecialInteger(self, arr):
        x=list(set(arr))
        for i in range(0,len(x)):
            #if ((arr.count(x[i])/len(arr))*100)>25:
            if arr.count(x[i])>len(arr)/4:
                return x[i]


