class Solution(object):
    def checkRecord(self, s):
        if(s.count('A')<2 and s.count('LLL')==0):
            return(True)
        else:
            return(False)
        