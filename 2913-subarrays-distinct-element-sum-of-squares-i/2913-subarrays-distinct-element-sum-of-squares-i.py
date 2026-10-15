class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        x=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)+1):
                x.append(len(set(nums[i:j]))**2)
        return sum(x)

                
                

