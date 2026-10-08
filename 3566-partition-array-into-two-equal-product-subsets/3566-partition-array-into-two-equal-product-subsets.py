class Solution(object):
    def checkEqualPartitions(self, nums, target):
        count=[0]
        y=[]
        def solve(i,x):
            if i>len(nums) or count[0]==1:
                return
            if i==len(nums):
                t=1
                for i in range(len(x)):
                    t=t*x[i]
                if t==target:
                    count[0]=count[0]+1
                    for i in range(len(x)):
                        y.append(x[i])
                return
            x.append(nums[i])
            solve(i+1,x)
            x.pop()
            solve(i+1,x)
        solve(0,[])
        if count[0]==1:
            for i in range(len(y)):
                nums.remove(y[i])
            z=1
            for i in range(len(nums)):
                z=z*nums[i]
            if z==target:
                return True
        return False
        