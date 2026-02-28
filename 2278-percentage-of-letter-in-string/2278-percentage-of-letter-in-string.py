class Solution(object):
    def percentageLetter(self, s, letter):
        count=0
        for ch in s:
            if ch==letter:
                count=count+1
        t=((count*100//len(s)))
        return t
        