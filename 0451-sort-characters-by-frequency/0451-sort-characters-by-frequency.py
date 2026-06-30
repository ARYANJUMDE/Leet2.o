class Solution(object):
    def frequencySort(self, s):
        # from collections import Counter
        # freq=Counter(s)
        # p=sorted(s,key=lambda x:(freq[x],x),reverse=True)
        # return(''.join(p))
        t=""
        x=[]
        for ch in s:
            if ch not in t:
                t=t+ch
        for i in range(len(t)):
            x.append([t[i],s.count(t[i])])
        x=sorted(x,key=lambda x:x[1],reverse=True)
        r=""
        for i in range(len(x)):
            r=r+x[i][0]*x[i][1]
        return(r)
