class Solution(object):
    def canBeEqual(self, target, arr):
        if (sorted(arr)==sorted(target)):
            return(True)
        else:
            return(False)

        