class Solution(object):
    def minWindow(self, s, t):
        # map1={}
        # min_len=float('inf')
        # start=-1
        # if len(t)>len(s):
        #     return("")
        # else:
        #     for i in range(len(t)):
        #         if t[i] not in map1:
        #             map1[t[i]]=1
        #         else:
        #             map1[t[i]]=map1[t[i]]+1
        #     k=map1.copy()
        #     for i in range(len(s)):
        #         k=map1.copy()
        #         count=0
        #         for j in range(i,len(s)):
        #             if s[j] in map1 and k[s[j]]>0:
        #                 count=count+1
        #                 k[s[j]]=k[s[j]]-1
        #             if count==len(t):
        #                 if j-i<min_len:
        #                     min_len=j-i
        #                     start=i
        #                 break
        #     if (start==-1):
        #         return("")
        #     else:
        #         return(s[start:(start+min_len+1)])

        map1={}
        min_len=float('inf')
        start=-1
        l=0
        r=0
        count=0
        if len(t)>len(s):
            return ""
        else:
            for i in range(len(t)):
                if t[i] not in map1:
                    map1[t[i]]=1
                else:
                    map1[t[i]]=map1[t[i]]+1
            while r<len(s):
                if s[r] in map1:
                    map1[s[r]]=map1[s[r]]-1
                    if map1[s[r]]>=0:
                        count=count+1
                while count==len(t):
                    if r-l+1<min_len:
                        min_len=r-l+1
                        start=l
                    if s[l] in map1:
                        map1[s[l]]=map1[s[l]]+1
                        if map1[s[l]]>0:
                            count=count-1
                    l=l+1
                r=r+1
        if start==-1:
            return ""
        else:
            return (s[start:(start+min_len)])
