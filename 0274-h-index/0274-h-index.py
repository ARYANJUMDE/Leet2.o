class Solution(object):
    def hIndex(self, citations):
        ans=0
        for i in range(1,len(citations)+1):
            count=0
            for j in range(len(citations)):
                if citations[j]>=i:
                    count=count+1
            if count>=i:
                ans=i
        
        return(ans)

        