class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        x_overlap=max(0,min(rec1[2],rec2[2])-max(rec1[0],rec2[0]))
        y_overlap=max(0,min(rec1[3],rec2[3])-max(rec1[1],rec2[1]))
        if(x_overlap*y_overlap>0):
            return(True)
        else:
            return(False)

        