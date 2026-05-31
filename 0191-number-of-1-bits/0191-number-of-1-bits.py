class Solution(object):
    def hammingWeight(self, n):
        s=bin(n)
        return s.count('1')
        