class Solution(object):
    def combinationSum(self, candidates, target):
        result=[]
        def solve(a,i,target):
            if target==0:
                result.append(a[:])
                return
            if target<0 or i==len(candidates):
                return
            else:
                a.append(candidates[i])
                solve(a,i,target-candidates[i])
                a.pop()
                solve(a,i+1,target)
        solve([],0,target)
        return result
        # result=[]
        # def backtrack(start, path, total):
        #     if total == target:
        #         result.append(path[:])
        #         return
        #     if total > target:
        #         return
        #     for i in range(start, len(candidates)):
                
        #         path.append(candidates[i])
        #         backtrack(i, path, total + candidates[i])
        #         path.pop()
        # backtrack(0, [], 0)
        # return result
        