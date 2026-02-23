class Solution(object):
    def mostWordsFound(self, sentences):
        x=[]
        for i in range(len(sentences)):
            x.append(len(sentences[i].split()))
        return(max(x))
        