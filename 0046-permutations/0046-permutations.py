from itertools import permutations
class Solution(object):
    def permute(self, nums):
        result=[]
        def solve(a,map1):
            if len(a)==len(nums):
                result.append(a[:])
                return
            else:
                for i in range(len(nums)):
                    if i not in map1:
                        a.append(nums[i])
                        map1.append(i)
                        solve(a,map1)
                        a.pop()
                        map1.pop()
        solve([],[])
        return result



        # x=[]
        # t=permutations(nums,len(nums))
        # for i in t:
        #     if i not in x:
        #         x.append(list(i))
        # return(x)



        