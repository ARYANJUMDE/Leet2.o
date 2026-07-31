class Solution(object):
    def minStartValue(self, nums):
        for i in range(1,9999):
            add=i
            count=0
            for j in range(len(nums)):
                add=add+nums[j]
                if add<1:
                    break
                else:
                    count=count+1
            if count==len(nums):
                return(i)

    