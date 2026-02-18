class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i=0
        x=0
        z=len(arr)
        while i<z:
            if(x!=z):
                if arr[i]==0:
                    arr.insert(i+1,0)
                    arr.pop()
                    x=x+2
                    i=i+2
                else:
                    x=x+1
                    i=i+1
