class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        count=0
        for i in range(0,len(arr1)):
            y=True
            for j in range(0,len(arr2)):
                x=abs(arr1[i]-arr2[j])
                if(x<=d):
                    y=False
                    break
            if(y==True):
                count=count+1
            
        return(count)
        