class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones.sort()
        x=len(stones)
        while x>1:
            if stones[-1]==stones[-2]:
                stones.pop(-1)
                stones.pop(-1)
                stones.sort()
            else:
                x=stones[-1]-stones[-2]
                stones.pop(-1)
                stones.pop(-1)
                stones.append(x)
                stones.sort()
            x=len(stones)
        
        if len(stones)==0:
            return 0
        return stones[0]

    