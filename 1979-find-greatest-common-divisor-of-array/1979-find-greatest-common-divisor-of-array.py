import math
class Solution(object):
    def findGCD(self, nums):
        x=max(nums)
        y=min(nums)
        z=[]
        p=[]
        for i in range(1,x+1):
            if(x%i==0):
                z.append(i)
        for j in range(1,y+1):
            if(y%j==0):
                p.append(j)
        curr=z[0]
        for i in range(1,len(z)):
            if z[i] in p:
                if curr<z[i]:
                    curr=z[i]
        return(curr)

