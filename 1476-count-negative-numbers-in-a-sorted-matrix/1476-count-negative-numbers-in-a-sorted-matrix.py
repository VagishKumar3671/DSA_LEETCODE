class Solution(object):
    def countNegatives(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        cn=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]<0:
                    cn+=1
        return cn