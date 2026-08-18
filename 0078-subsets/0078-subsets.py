class Solution(object):
    def subsets(self, nums):
        result=[]
        def solve(a,i):
            if i==len(nums):
                result.append(a[:])
                return 
            else:
                a.append(nums[i])
                solve(a,i+1)
                a.pop()
                solve(a,i+1)
        solve([],0)
        return result

        

        # from itertools import combinations
        # t=[]
        # for i in range(0,len(nums)+1):
        #     for com in combinations(nums,i):
        #         t.append(list(com))
        # return (t)


# len(nums) = length of the list. For [1,2,3], it’s 3.

# range(len(nums)+1) = range(4) = [0, 1, 2, 3].

# So r takes values: 0, 1, 2, 3.

# Meaning: we will generate subsets of size 0, size 1, size 2, size 3.
# combinations(nums, r) generates all subsets of length r.

# Example:

# If r = 0 → [()] (just the empty subset).

# If r = 1 → [(1), (2), (3)].

# If r = 2 → [(1,2), (1,3), (2,3)].

# If r = 3 → [(1,2,3)].

# combo is a tuple, e.g. (1,2).