class Solution(object):
    def numberOfPairs(self, nums):
        x=[]
        for num in nums:
            if num not in x:
                x.append(num)
        y=[]
        for num in x:
            y.append(nums.count(num))
        count=0
        z=0
        for i in range(len(y)):
            
            if y[i]%2==0:
                count=count+y[i]//2
            else:
                
                count=count+(y[i]-1)//2
                z=z+1
        t=[count,z]
        return(t)

        