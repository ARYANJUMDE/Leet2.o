class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n<10:
            return False
        else:
            i=10
            count=0
            while n>=i:
                n=n-i
                i=i-1
                count=count+1
            if count%2!=0:
                return True
            return False

        
        