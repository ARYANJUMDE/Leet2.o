class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        count=0
        l=0
        r=0
        while l<len(s) and r<len(g):
            if s[l]>=g[r]:
                count=count+1
                r=r+1
            l=l+1
        return count
        # count=0
        # for i in range(len(g)):
        #     for j in range(len(s)):
        #         if g[i]<=s[j]:
        #             count=count+1
        #             s.remove(s[j])
        #             break
        
        
        # return(count)
        return count

        