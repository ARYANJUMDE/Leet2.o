class Solution(object):
    def minMoves(self, nums):
        moves=0
        nums.sort()
        maxi=nums[-1]
        for i in range(len(nums)-1):
            moves=moves+maxi-nums[i]
        return moves
        