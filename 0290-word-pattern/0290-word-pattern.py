class Solution(object):
    def wordPattern(self, pattern, s):
        x=[]
        y=[]
        x=s.split()
        t=[]
        if len(pattern)!=len(x):
            return False
        for ch2 in x:
            if ch2 not in t:
                t.append(ch2)

        for ch in pattern:
            if ch not in y:
                y.append(ch)
        if(len(t)!=len(y)):

            return False
        for i in range(len(pattern)):
            if(y.index(pattern[i])!=t.index(x[i])):
                return False
        return True

        