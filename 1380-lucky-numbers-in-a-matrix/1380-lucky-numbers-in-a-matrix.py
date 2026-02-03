class Solution(object):
    def luckyNumbers(self, matrix):
        row_min=[]
        col_max=[]
        for i in range(len(matrix)):
            row_min.append(min(matrix[i]))
        for j in range(len(matrix[0])):
            max_val=matrix[0][j]
            for i in range(len(matrix)):
                if matrix[i][j]>max_val:
                    max_val=matrix[i][j]
            col_max.append(max_val)
            
        res=[]
        for num in row_min:
            if num in col_max:
                
                res.append(num)
        return res
        