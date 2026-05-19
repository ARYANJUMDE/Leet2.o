class Solution(object):
    def countCharacters(self, words, chars):
        x=0
        for i in range(len(words)):
            if all(words[i].count(ch) <= chars.count(ch) for ch in words[i]):
                x=x+len(words[i])
        
        
        return(x)

        