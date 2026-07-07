class Solution(object):
    def sumAndMultiply(self, n):
        s=str(n)
        t=""
        p=0
        for ch in s:
            if ch!="0":
                t=t+ch
                p=p+int(ch)
        
        
        return(int(t)*p)

        