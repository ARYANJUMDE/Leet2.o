class Solution(object):
    def maximumNumber(self, num, change):
        x=[]
        y=[]
        for i in range(len(num)):
            x.append(int(num[i]))
        for i in range(len(num)):
            y.append(change[int(num[i])])
        z=[]
        for i in range(len(x)):
            if x[i]<y[i]:
                z.append(i)
        if len(z)>0:
            start=z[0]
            for i in range(start,len(x)):
                if x[i]<=y[i]:
                    x[i]=y[i]
                else:
                    break
        t=""
        for i in range(len(x)):
            t=t+str(x[i])
        return t

        # x=[]
        # y=[]
        # for i in range(len(num)):
        #     x.append(change[int(num[i])])
        # for i in range(len(num)):
        #     y.append(int(num[i]))
        # i=0
        # j=0
        # z=[]
        # while j<len(x):
        #     if x[j]>y[j]:
        #         j=j+1
        #     else:
        #         if i!=j:
        #             z.append([i,j-1])
        #         j=j+1
        #         while i!=j:
        #             i=i+1
        # z.append([i,j-1])
        # if len(z)>0:
        #     for i in range(z[0][0],z[0][1]+1):
        #         y[i]=x[i]
        # st=""
        # for i in range(len(y)):
        #     st=st+str(y[i])
        # return(st)

        