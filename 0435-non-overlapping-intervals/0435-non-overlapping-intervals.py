class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        # intervals.sort(key=lambda t:t[0])
        # count=0
        # for i in range(len(intervals)-1):
        #     if intervals[i][1]>=intervals[i+1][1]:
        #         count=count+1
        
        # return(count)
        t=len(intervals)
        intervals=sorted(intervals,key=lambda x:(x[0]))
        for i in range(len(intervals)-1):
            if intervals[i][0]==intervals[i+1][0] and intervals[i][1]>intervals[i+1][1]:
                intervals[i],intervals[i+1]=intervals[i+1],intervals[i]
        i=0
        while i<len(intervals)-1:
            if intervals[i+1][0]<intervals[i][1]:
                if intervals[i][1]<=intervals[i+1][1]:
                    intervals.pop(i+1)
                else:
                    intervals.pop(i)
                i=i
            else:
                i=i+1
        return t-len(intervals)
