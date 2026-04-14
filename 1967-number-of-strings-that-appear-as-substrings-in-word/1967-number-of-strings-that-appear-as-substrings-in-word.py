class Solution(object):
    def numOfStrings(self, patterns, word):
        count=0
        for ch in patterns:
            if ch in word:
                count=count+1
        
        
        return(count)
        