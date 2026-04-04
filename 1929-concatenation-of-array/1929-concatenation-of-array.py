class Solution(object):
    def getConcatenation(self, nums):
        x=[]
        for num in nums:
            x.append(num)
        y=nums+x
        return(y)