class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if(len(flowerbed)==1):
            if flowerbed[0]==0:
                n=n-1
            return n<=0
        if flowerbed[0]==0 and flowerbed[1]==0:
            flowerbed[0]=1
            n=n-1
        for i in range(len(flowerbed)-2):
            if(flowerbed[i]==0 and flowerbed[i+2]==0 and flowerbed[i+1]!=1):
                flowerbed[i+1]=1
                n=n-1
                if(n==0):
                    return(True)
        if(flowerbed[-1]==0 and flowerbed[-2]==0):
            
            n=n-1
        return n<=0


        