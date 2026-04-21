class Solution(object):
    def sortPeople(self, names, heights):
        x=[]
        for i in range (len(names)):
            x.append([names[i],heights[i]])
        x.sort(key=lambda t:t[1],reverse=True)
        y=[]
        for i in range(len(x)):
            y.append(x[i][0])
        
        
        return(y)


        