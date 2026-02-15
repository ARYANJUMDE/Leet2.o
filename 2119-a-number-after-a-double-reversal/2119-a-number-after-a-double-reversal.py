class Solution(object):
    def isSameAfterReversals(self, num):
        x=str(num)
        x=x[::-1]
        y=int(x)
        z=str(y)
        z=z[::-1]
        r=int(z)
        if(r==num):
            return(True)
        else:
            return(False)
        