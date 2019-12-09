# https://leetcode.com/problems/number-of-islands/
# 200. Number of Islands
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(grid,row,col):
            if (row<0 or row>len(grid)-1) or (col<0 or col>len(grid[0])-1) or grid[row][col]=="0":
                return 
            
            grid[row][col]='0'
            dfs(grid,row+1,col)
            dfs(grid,row-1,col)
            dfs(grid,row,col+1)
            dfs(grid,row,col-1)
        
        
        
        count=0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    count+=1
                    dfs(grid,i,j)
                    
                    
        return count 