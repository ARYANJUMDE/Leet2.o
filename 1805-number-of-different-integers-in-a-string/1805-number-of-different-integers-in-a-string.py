class Solution(object):
    def numDifferentIntegers(self, word):
        x=[]
        t=[]
        for i in range(97,123):
            x.append(chr(i))
        for i in range(len(word)):
            if word[i] in x:
                word=word.replace(word[i]," ")
        i=0
        while i<(len(word)):
            if word[i]!=" ":
                p=word[i]
                j=i
                for j in range(i+1,len(word)):  
                    if word[j]!=" ":
                        p=p+word[j]
                    else:
                        if int(p) not in t:
                            t.append(int(p))
                        break
                else:
                    if int(p) not in t:
                        t.append(int(p))
                i=j+1
            else:
                i=i+1
        return(len(t))

    
        