class Solution(object):
    def minSumOfLengths(self, arr, target):
        r=0
        l=0
        sum1=0
        count=0
        x=[]
        while r<len(arr):
            sum1=arr[r]+sum1
            if sum1==target:
                x.append([r-l+1,l,r])
            if sum1>target:
                while sum1>target:
                    sum1=sum1-arr[l]
                    l=l+1
                    if sum1==target:
                        x.append([r-l+1,l,r])
            r=r+1
        if len(x)<2:
            return -1
        else:
            x.sort(key=lambda t: t[2])
            ans = float('inf')
            min_len = float('inf')
            j = 0
            for i in range(len(x)):
                while j < len(x) and x[j][2] < x[i][1]:
                    min_len = min(min_len, x[j][0])
                    j = j + 1
                if min_len != float('inf'):
                    ans = min(ans, min_len + x[i][0])
            if ans == float('inf'):
                 return -1
            return ans
                


