class Solution(object):
    def maximumValue(self, strs):
        x=[]
        for i in range(len(strs)):
            if strs[i].isdigit():
                x.append(int(strs[i]))
            else:
                
                x.append(len(strs[i]))
        return(max(x))
        