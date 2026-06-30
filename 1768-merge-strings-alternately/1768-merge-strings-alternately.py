class Solution(object):
    def mergeAlternately(self, word1, word2):
        t=""
        v=""
        z=abs(len(word1)-len(word2))
        if z!=0:
            if min(len(word1),len(word2))==len(word1):
                for i in range(z):
                    word1=word1+" "
            else:
                for i in range(z):
                    word2=word2+" "
        for i in range(len(word1)):
            t=t+word1[i]
            t=t+word2[i]
        for i in range(len(t)):
            if t[i]!=" ":
                v=v+t[i]
        return(v)

        