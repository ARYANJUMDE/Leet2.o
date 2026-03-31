class Solution(object):
    def findLucky(self, arr):
        x=[]
        y=[]
        for num in arr:
            if num not in x:
                x.append(num)
        for num in x:
            if num==arr.count(num):
                y.append(num)
        if(len(y)==0):
            return(-1)
        
        else:
            return(max(y))

        