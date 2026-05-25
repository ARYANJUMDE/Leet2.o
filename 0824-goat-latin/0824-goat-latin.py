class Solution(object):
    def toGoatLatin(self, sentence):
        x=sentence.split()
        z=["a","e","i","o","u","A","E","I","O","U"]
        for i in range(len(x)):
            if x[i][0] in z:
                x[i]=x[i]+"ma"+(i+1)*"a"
            else:
                t=x[i][0]
                x[i]=x[i].replace(x[i][0],"",1)
                x[i]=x[i]+t+"ma"+(i+1)*"a"
        return " ".join(x)