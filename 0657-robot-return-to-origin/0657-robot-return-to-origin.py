class Solution(object):
    def judgeCircle(self, moves):
        x=moves.count('U')
        y=moves.count('D')
        z=moves.count('L')
        m=moves.count('R')
        if(x==y and z==m):
            return(True)
        else:
            return(False)

        