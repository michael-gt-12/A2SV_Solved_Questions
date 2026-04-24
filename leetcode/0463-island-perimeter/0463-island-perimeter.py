class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        def inbound(row,col):
            return (0 <= row and row < rows) and (0 <= col and col < cols)
        
        visited = [[False for _ in range(cols)]for _ in range(rows)]

        def dfs(grid,visited,row,col):

            if not inbound(row,col):
                return 1
            if grid[row][col] == 0:
                return 1
            if visited[row][col]:
                return 0

            visited[row][col] = True

            perimeter = 0
            for row_change , col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                perimeter +=  dfs(grid, visited, new_row, new_col)

            return perimeter

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(grid,visited,i,j)
        
        return 0
        
        