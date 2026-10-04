class Solution(object):
    def arrayRankTransform(self, arr):
        x=list(set(arr))
        x.sort()
        y={}
        for i in range(len(x)):
            if x[i] not in y:
                y[x[i]]=i+1
        z=[]
        for i in range(len(arr)):
            z.append(y[arr[i]])
        return(z)
        # y=[]
        # for i in range(len(arr)):
        #     y.append(x.index(arr[i])+1)
        # return(y)
        # # x=[]
        # y=[]
        # for i in range(len(arr)):
        #     x.append(arr[i])
        # t=[]
        # for i in range(len(arr)):
        #     if arr[i] not in t:
        #         t.append(arr[i])
        # t.sort()
        # for i in range(len(x)):
        #     y.append(t.index(x[i])+1)
        # return y