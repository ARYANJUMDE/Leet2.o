class Solution(object):
    def twoCitySchedCost(self, costs):
        costs=sorted(costs,key=lambda x:x[0]-x[1])
        cost1=0
        cost2=0
        for i in range(len(costs)//2):
            cost1=cost1+costs[i][0]
        for j in range(len(costs)//2,len(costs)):
            cost2=cost2+costs[j][1]
        return cost1+cost2
        # s1=[]
        # s2=[]
        # for i in range(len(costs)):
        #     s1.append(costs[i][0])
        #     s2.append(costs[i][1])
        # cost1=0
        # cost2=0
        # while len(s2)!=0:
        #     t=min(s1)
        #     p=s1.index(t)
        #     cost1=cost1+t
        #     s1.pop(p)
        #     s2.pop(p)
        #     z=min(s2)
        #     q=s2.index(z)
        #     cost2=cost2+z
        #     s2.pop(q)
        #     s1.pop(q)
        # return cost1+cost2

        