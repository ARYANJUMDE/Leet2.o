class Solution(object):
    def removeCoveredIntervals(self, intervals):
        intervals=sorted(intervals,key=lambda x:(x[0],-x[1]))
        i=0
        while i<(len(intervals)-1):
            if intervals[i][0]<=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][1]:
                intervals[i]=[intervals[i][0],intervals[i][1]]
                intervals.pop(i+1)
            else:
                i=i+1
        
        return(len(intervals))

