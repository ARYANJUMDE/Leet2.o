class Solution(object):
    def maxNumberOfBalloons(self, text):
        p="balloon"
        t={}
        for ch in text:
            if ch in  p:
                if ch not in t:
                    t[ch]=1
                else:
                    t[ch]=t[ch]+1
        count=0
        o=True
        while o:
            for ch in p:
                if ch in t:
                    if t[ch]!=0:
                        t[ch]=t[ch]-1
                    else:
                        o=False
                        break
                else:
                    o=False
                    break
                if ch=='n':
                    count=count+1
        return(count)
