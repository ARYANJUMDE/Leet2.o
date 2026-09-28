class Solution(object):
    def minimumSum(self, n, k):
        x=set()
        i=1
        while len(x)<n:
            if (k-i) not in x:
                x.add(i)
            i=i+1
        return sum(x)
        # x=[]
        # for i in range(1,n+1):
        #     x.append(i)
        # new_num=n+1
        # for i in range(len(x)):
        #     t=k-x[i]
        #     if t in x and x.index(t)!=i:
        #         index=x.index(t)
        #         if i<index:
        #             o=x.pop(index)
        #         else:
        #             p=x.pop(i)
        #         x.append(new_num)
        #         new_num=new_num+1
        # return sum(x)
    
