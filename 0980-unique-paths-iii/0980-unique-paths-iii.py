class Solution(object):
    def uniquePathsIII(self, grid):
        m = len(grid)
        n = len(grid[0])
        empty = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    empty += 1
                if grid[i][j] == 1:
                    sx, sy = i, j
        self.ans = 0
        
        
        def dfs(x, y, count):
            if x < 0 or y < 0 or x >= m or y >= n or grid[x][y] == -1:

                return
            if grid[x][y] == 2:
                if count == empty:   
                    self.ans += 1
                return
            temp = grid[x][y]
            grid[x][y] = -1
            
            dfs(x+1, y, count+1)
            dfs(x-1, y, count+1)
            dfs(x, y+1, count+1)
            dfs(x, y-1, count+1)
            
            
            grid[x][y] = temp
        
    
        dfs(sx, sy, 1)
        return self.ans
        