class Solution(object):
    def checkString(self, s):
        x=[]
        for i in range(len(s)):
            if len(x)==0 and s[i]=='a':
                x.append(i)
            else:
                if s[i]=='a':
                    if i-x[-1]!=1:
                        return False
                    else:
                        x.append(i)
        if len(x)>0 and x[0]!=0:
            return False
        return True