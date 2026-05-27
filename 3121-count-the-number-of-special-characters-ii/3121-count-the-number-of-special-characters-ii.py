class Solution(object):
    def numberOfSpecialChars(self, word):
        x=[]
        y=[]
        count=0
        for i in range(97,123):
            x.append(chr(i))
        for j in range(65,91):
            y.append(chr(j))
        s=""
        for ch in word:
            if ch not in s:
                s=s+ch
        for i in range(len(x)):
            if (x[i] in s and y[i] in s) and (word.rindex(x[i])<word.index(y[i])):
                count=count+1
        
        return(count)
            

        
        