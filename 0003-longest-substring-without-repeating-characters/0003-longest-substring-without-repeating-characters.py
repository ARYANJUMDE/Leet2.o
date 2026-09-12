class Solution(object):
    def lengthOfLongestSubstring(self, s):
        curr_len=0
        final_len=0
        l=0
        r=0
        t=[]
        while r<len(s):
            if s[r] in t:
                while s[r] in t:
                    t.pop(0)
                    l=l+1
                    curr_len=curr_len-1
            t.append(s[r])
            curr_len=curr_len+1
            if curr_len>final_len:
                final_len=curr_len
            r=r+1
        return(final_len)
#         n = len(s)
#         max_len = 0
#         for i in range(n):
#             seen = set()
#             curr_len = 0
#             for j in range(i, n):
#                 if s[j] in seen:   
#                     break
#                 seen.add(s[j])
#                 curr_len += 1
#                 max_len = max(max_len, curr_len)
#         return max_len



# S=Solution()
# S.lengthOfLongestSubstring("abcabcbb")      
        