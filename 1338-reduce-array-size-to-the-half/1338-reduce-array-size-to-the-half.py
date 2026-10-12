class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        x={}
        t=len(arr)//2
        for i in range(len(arr)):
            if arr[i] not in x:
                x[arr[i]]=1
            else:
                x[arr[i]]=x[arr[i]]+1
        x=dict(sorted(x.items(),key=lambda x:x[1],reverse=True))
        count=0
        sum1=0
        for ch in x:
            sum1=sum1+x[ch]
            count=count+1
            if sum1>=(t):
                break
        return(count)

        