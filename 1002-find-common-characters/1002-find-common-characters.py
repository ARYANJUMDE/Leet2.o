class Solution(object):
    def commonChars(self, words):
        t=words[0]
        z=""
        x=[]
        for ch in t:
            if ch not in z:
                z=z+ch
        for i in range(len(z)):
            p=[]
            for j in range(len(words)):
                p.append(words[j].count(z[i]))
            if min(p)>0:
                x.extend((z[i]*min(p)))
        return(x)

        