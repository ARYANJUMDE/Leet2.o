class Solution(object):
    def getMaximumConsecutive(self, coins):
        # reach=0
        # coins.sort()
        # for i in range(len(coins)):
        #     if coins[i]>reach+1:
        #         break
        #     reach=reach+coins[i]
        # return reach+1
        coins.sort()
        # a=[0]
        # s=set()
        # for i in range(len(coins)):
        #     for j in range(len(a)):
        #         t=a[j]+coins[i]
        #         if t not in s:
        #             a.append(t)
        #             s.add(t)
        #         if a[-2]!=a[-1]-1:
        #             a.pop()
        #             break
        # return(len(a))
        coins.sort()
        max_val=0
        for i in range(len(coins)):
            if max_val+1<coins[i]:
                break
            max_val=max_val+coins[i]
        return max_val+1
                    