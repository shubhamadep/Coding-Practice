class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid == []:
            return 0
        nr = len(grid)
        nc = len(grid[0])
        num_of_islands = 0

        for i in range(0, nr):
            for j in range(0, nc):

                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    num_of_islands += 1


        return num_of_islands

    def dfs(self, grid, r, c):

        nr = len(grid)
        nc = len(grid[0])

        grid[r][c] = '0'

        if r+1 < nr and grid[r+1][c] == '1':
            self.dfs(grid, r+1, c)
        if r-1 >= 0 and grid[r-1][c] == '1':
            self.dfs(grid, r-1, c)
        if c-1 >= 0 and grid[r][c-1] == '1':
            self.dfs(grid, r, c-1)
        if c+1 < nc and grid[r][c+1] == '1':
            self.dfs(grid, r, c+1)
        
