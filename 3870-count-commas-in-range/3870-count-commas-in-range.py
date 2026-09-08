class Solution(object):
    def countCommas(self, n):
        x=str(n)
        if len(x)<4:
            return 0
        else:
            return n-1000+1
        