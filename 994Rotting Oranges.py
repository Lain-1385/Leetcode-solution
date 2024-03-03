from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length_row = len(grid)
        length_column = len(grid[0])
        bfs = deque()
        flag_fresh = 0
        for m in range(0, len(grid)):
            for n in range(0, len(grid[0])):
                if grid[m][n] == 2:
                    bfs.append((m, n, 0))
                    grid[m][n] = 0
                if flag_fresh == 0 and grid[m][n] == 1:
                    flag_fresh = 1
                    
        if not bfs and not flag_fresh:
            return 0
        if not bfs and flag_fresh:
            return -1
        while bfs:
            cur_row, cur_column, cur_time = bfs.popleft()
            cur_time += 1 
            if cur_column > 0 and grid[cur_row][cur_column - 1] == 1:
                bfs.append((cur_row, cur_column - 1, cur_time))
                grid[cur_row][cur_column - 1] = 0
            if cur_row > 0 and grid[cur_row - 1][cur_column] == 1:
                bfs.append((cur_row - 1, cur_column, cur_time))
                grid[cur_row - 1][cur_column] = 0
            if cur_column + 1 < length_column and grid[cur_row][cur_column + 1] == 1:
                bfs.append((cur_row, cur_column + 1, cur_time))
                grid[cur_row][cur_column + 1] = 0
            if cur_row + 1 < length_row and grid[cur_row + 1][cur_column] == 1:
                bfs.append((cur_row + 1, cur_column, cur_time))
                grid[cur_row+1][cur_column] = 0
        for m in range(0, len(grid)):
            for n in range(0, len(grid[0])):
                if grid[m][n] == 1:
                    return -1
        return cur_time - 1 