class Solution(object):
    def reconstructQueue(self, people):
        people=sorted(people,key=lambda x:(-x[0],x[1]))
        x=[]
        for i in range (len(people)):
            x.insert(people[i][1],people[i])
        
        
        return(x)
        