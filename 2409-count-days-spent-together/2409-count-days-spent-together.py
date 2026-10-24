class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        if leaveAlice<arriveBob or leaveBob<arriveAlice:
            return(0)
        else:
            start=max(arriveAlice,arriveBob)
            end=min(leaveAlice,leaveBob)
            months=[31,28,31,30,31,30,31,31,30,31,30,31]
            return sum(months[:int(end[:2])-1]) + int(end[3:]) - sum(months[:int(start[:2])-1]) - int(start[3:]) + 1

        