class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def island_to_water(row, column, grid: List[List[str]]):
            length_row = len(grid)
            length_column = len(grid[0])
            dfs = []
            dfs.append((row, column))
            while dfs:
                cur_row, cur_column = dfs.pop()
                grid[cur_row][cur_column] = "0"
                if cur_column > 0 and grid[cur_row][cur_column - 1] == "1":
                    dfs.append((cur_row, cur_column - 1)) 
                if cur_row > 0 and grid[cur_row - 1][cur_column] == "1":
                    dfs.append((cur_row - 1, cur_column))
                if cur_column + 1 < length_column and grid[cur_row][cur_column + 1] == "1":
                    dfs.append((cur_row, cur_column + 1))
                if cur_row + 1 < length_row and grid[cur_row + 1][cur_column] == "1":
                    dfs.append((cur_row + 1, cur_column))
        res = 0
        for m in range(0, len(grid)):
            for n in range(0, len(grid[0])):
                if grid[m][n] == "1":
                    island_to_water(m, n, grid)
                    res += 1
        return res