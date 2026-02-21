class Solution(object):
    def countPrimeSetBits(self, left, right):
        x=[]
        y=[]
        for i in range(left,right+1):
            x.append(bin(i)[2:])
        for bi in x:
            y.append(bi.count('1'))
        count2=0
        for num in y: 
            count1=0
            for i in range(1,num+1):
                if num%i==0:
                    count1=count1+1
            if(count1==2):
                count2=count2+1
        
        return(count2)
    

        