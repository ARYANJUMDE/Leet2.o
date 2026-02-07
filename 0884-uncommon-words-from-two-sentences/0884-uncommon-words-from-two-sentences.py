class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        x=[]
        y=s1.split()
        z=s2.split()
        for word in y:
            if word not in z and y.count(word)<2:
                x.append(word)
        for word in z:
            if word not in y and z.count(word)<2:
                x.append(word) 
        return(x)
        