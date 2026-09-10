class Solution(object):
    def reverseBits(self, n):
        t=bin(n)[2:].zfill(32)
        z=t[::-1]
        return int(z,2)
        