class Solution(object):
    def searchMatrix(self, matrix, target):
        for i in range(len(matrix)):
            low=0
            high=len(matrix[i])-1
            while low<=high:
                mid=(low+high)//2
                if(matrix[i][mid]==target):
                    return(True)
                elif(matrix[i][mid]>target):
                    high=mid-1
                else:

                    low=mid+1
        else:
             return(False)


        