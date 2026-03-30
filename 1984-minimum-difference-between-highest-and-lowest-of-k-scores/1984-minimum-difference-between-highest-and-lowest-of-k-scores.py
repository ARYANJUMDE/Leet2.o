from itertools import combinations
class Solution(object):
    def minimumDifference(self, nums, k):
        # x=[]
        # y=[]
        # x.extend(combinations(nums,k))            
        # for i in range(len(x)):
        #     y.append(max(x[i])-min(x[i]))
        # return(min(y))
        nums.sort()
        # x=[]
        # y=[]
        
        # for i in range(k):
        #     x.append(nums[i])
        # nums.sort(reverse=True)
        
        # for i in range(k):
        #     y.append(nums[i])
        # t=max(x)-min(x)
        # p=max(y)-min(y)
        # return(min(t,p))
        min_diff=float('inf')
        for i in range(len(nums)-k+1):
            diff=nums[i+k-1]-nums[i]
            min_diff=min(min_diff,diff)
        return min_diff
        
