class Solution(object):
    def combinationSum2(self, candidates, target):
        y=[]
        def solve(x,i,sum1):
            if i>len(candidates) or sum1>target:
                return
            if i==len(candidates):
                if sum1==target:
                    if sorted(x) not in y:
                        y.append(sorted(x[:]))
                return
            x.append(candidates[i])
            sum1=sum1+candidates[i]
            solve(x,i+1,sum1)
            sum1=sum1-candidates[i]
            x.pop()
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i=i+1
            solve(x,i+1,sum1)
        solve([],0,0)
        return y
        