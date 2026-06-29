class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals=sorted(intervals,key=lambda x:x[0])
        i=0
        while i<len(intervals)-1:
            if intervals[i][1]>=intervals[i+1][0]:
                intervals.insert(i,[intervals[i][0],max(intervals[i+1][1],intervals[i][1])])
                intervals.pop(i+1)
                intervals.pop(i+1)
                i=i-1
            i=i+1
        
        return(intervals)
