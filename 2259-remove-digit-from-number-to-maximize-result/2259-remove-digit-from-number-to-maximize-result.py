class Solution(object):
    def removeDigit(self, number, digit):
        x=[]
        y=[]
        for i in range(len(number)):
            if number[i]==digit:
                x.append(i)
        for i in range(len(x)):
            y.append(int(number[:x[i]]+""+number[x[i]+1:]))
        return str((max(y)))

        