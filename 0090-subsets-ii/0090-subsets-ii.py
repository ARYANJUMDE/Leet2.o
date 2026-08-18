class Solution(object):
    def subsetsWithDup(self, nums):
        result=[]
        def solve(a,i):
            if i==len(nums):
                if sorted(a) not in result:
                    result.append(sorted(a[:]))
                return 
            else:
                a.append(nums[i])
                solve(a,i+1)
                a.pop()
                solve(a,i+1)
        solve([],0)
        return (result)

        # x=[[]]
        # for i in range(len(nums)):
        #     if [nums[i]] not in x:
        #         x.append([nums[i]])
        # for i in range(len(nums)-1):
        #     t=[nums[i]]
        #     for j in range(i+1,len(nums)):
        #         t=t+[nums[j]]
        #         if t not in x:
        #             x.append(t)
        
        # return(x)
