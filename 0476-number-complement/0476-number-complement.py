class Solution(object):
    def findComplement(self, num):
        z=bin(num)[2:]
        p=""
        for i in range(len(z)):
            if z[i] =="0":
                p=p+"1"
            else:
                p=p+"0"
        return int(p,2)
        