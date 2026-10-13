class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        x=[]
        for i in range(len(nums)):
            x.append(abs(nums[i]))
        x.sort(reverse=True)
        if len(x)%2==0:
            y=x[:len(x)//2]
            z=x[len(x)//2:]
            sum1=0
            sum2=0
            for i in range(len(y)):
                sum1=sum1+y[i]*y[i]
            for i in range(len(z)):
                sum2=sum2+z[i]*z[i]
            return(sum1-sum2)
        else:
            y=x[:len(x)//2+1]
            z=x[len(x)//2+1:]
            sum1=0
            sum2=0
            for i in range(len(y)):
                sum1=sum1+y[i]*y[i]
            for i in range(len(z)):
                sum2=sum2+z[i]*z[i]
            return(sum1-sum2)
