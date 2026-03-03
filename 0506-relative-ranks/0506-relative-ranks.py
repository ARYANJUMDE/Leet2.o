class Solution(object):
    def findRelativeRanks(self, score):
        x=[]
        y=sorted(score)
        t=sorted(score,reverse=True)
        for i in range(len(score)):
            if(score[i] not in x):
                if(score[i]==max(score)):
                    x.append('Gold Medal')
                elif(score[i]==y[-2]):
                    x.append('Silver Medal')
                elif(score[i]==y[-3]):
                    x.append('Bronze Medal')
                else:
                    x.append(str(t.index(score[i])+1))
        return(x)

        