class Solution(object):
    def checkOnesSegment(self, s):
        x=[]
        y=[]
        for i in range(len(s)):
            if s[i]=='1':
                x.append(i)
            else:
                y.append(i)
        for num in y:
            if num+1 in x:
                return(False)
                
        else:
            return(True) 


                    

        