class Solution(object):
    def shuffle(self, nums, n):
        x=[]
        y=[]
        z=[]
        for i in range(0,n):
            x.append(nums[i])
        for i in range(n,len(nums)):
            y.append(nums[i])
        i=0
        while len(y)>0:
            if i%2==0:
                z.append(x[0])
                x.pop(0)
            else:
                z.append(y[0])
                y.pop(0)
            i=i+1
        return z
