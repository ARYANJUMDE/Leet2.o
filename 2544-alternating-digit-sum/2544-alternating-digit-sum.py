class Solution(object):
    def alternateDigitSum(self, n):
        st=str(n)
        x=[]
        for i in range(len(st)):
            if i%2!=0:
                x.append(int("-"+st[i]))
            else:
                x.append(int(st[i]))
        return(sum(x))
        