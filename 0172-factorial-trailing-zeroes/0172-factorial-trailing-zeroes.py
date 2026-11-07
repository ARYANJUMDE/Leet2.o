class Solution(object):
    def trailingZeroes(self, n):
        n1=1
        for i in range(1,n+1):
            n1=n1*i
        count=0
        st=str(n1)
        for i in range(len(st)-1,-1,-1):
            if st[i]=='0':
                count=count+1
            else:
                break
        return count