class Solution:
    def check(self, nums: list[int]) -> bool:
        if nums==sorted(nums):
            return True
        else:
            t=len(nums)
            for i in range(t):
                x=nums.pop(0)
                nums.append(x)
                if nums==sorted(nums):
                    return True
        return False
        