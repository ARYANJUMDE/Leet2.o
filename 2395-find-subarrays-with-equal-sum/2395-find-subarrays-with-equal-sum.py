class Solution(object):
    def findSubarrays(self, nums):
        r=0
        s=[]
        l=0
        sum1=0
        curr_len=0
        while r<len(nums):
            sum1=sum1+nums[r]
            curr_len=curr_len+1
            if curr_len>2:
                while curr_len>2:
                    sum1=sum1-nums[l]
                    curr_len=curr_len-1
                    l=l+1
            if curr_len==2:
                s.append(sum1)
            r=r+1
        if len(s)==len(set(s)):
            return False
        if len(s)>len(set(s)):
            return True
            

        