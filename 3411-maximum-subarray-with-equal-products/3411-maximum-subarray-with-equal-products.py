class Solution:
    def maxLength(self, nums: List[int]) -> int:
        from math import gcd,lcm
        max_len=float('-inf')
        for i in range(len(nums)):
            prod=1
            x=[]
            for j in range(i,len(nums)):
                prod=prod*nums[j]
                x.append(nums[j])
                g=math.gcd(*x)
                l=math.lcm(*x)
                if prod==g*l:
                    if j-i+1>max_len:
                        max_len=j-i+1
        return max_len


        