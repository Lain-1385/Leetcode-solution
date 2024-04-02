from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        length_row = len(grid)
        length_column = len(grid[0])
        bfs = deque()
        cnt_fresh = 0
        for m in range(0, len(grid)):
            for n in range(0, len(grid[0])):
                if grid[m][n] == 2:
                    bfs.append((m, n, 0))
                    grid[m][n] = 0
                if grid[m][n] == 1:
                    cnt_fresh += 1
                    
        if not bfs and not cnt_fresh:
            return 0
        if not bfs and cnt_fresh:
            return -1
        directions = [[0,1], [1,0], [0, -1], [-1, 0]]
        while bfs:
            cur_row, cur_column, cur_time = bfs.popleft()
            cur_time += 1

            for dx, dy in directions:
                new_row, new_column = cur_row + dx, cur_column + dy
                if new_row < 0 or new_row == length_row or new_column < 0 or new_column == length_column or grid[new_row][new_column] != 1:
                    continue
                grid[new_row][new_column] = 0
                bfs.append((new_row, new_column, cur_time))
                cnt_fresh -= 1

        return -1 if cnt_fresh else cur_time -1
