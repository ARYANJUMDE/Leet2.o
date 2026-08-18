class Solution(object):
    def findSubsequences(self, nums):
        result=[]
        def solve(a,i):
            if i==len(nums):
                if len(a)>=2 and a==sorted(a,reverse=False) and a not in result  :
                    result.append(a[:])
                    return
            else:
                a.append(nums[i])
                solve(a,i+1)
                a.pop()
                solve(a,i+1)
        solve([],0)
        return result