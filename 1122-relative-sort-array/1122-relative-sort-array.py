class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        x=[]
        y=[]
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i]==arr1[j]:
                    x.append(arr2[i])
        arr1.sort()
        for num in arr1:
            if num not in x:
                y.append(num)          
        
        return(x+y)
