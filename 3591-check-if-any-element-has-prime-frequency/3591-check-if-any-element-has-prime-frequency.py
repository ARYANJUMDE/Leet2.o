class Solution(object):
    def checkPrimeFrequency(self, nums):
        x=[]
        for num in nums:
            if num not in x:
                x.append(num)
        y=[]
        for num in x:
            y.append(nums.count(num))
        for i in range(len(y)):
            count=0
            for j in range(1,y[i]+1):
                if y[i]%j==0:
                    count=count+1
            if count==2:
                return(True)
        else:
            return(False)

        