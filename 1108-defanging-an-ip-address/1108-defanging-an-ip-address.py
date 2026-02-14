class Solution(object):
    def defangIPaddr(self, address):
        x=''
        for ch in address:
            if ch=='.':
                x=x+'[.]'
            else:
                x=x+ch
        return(x)
        