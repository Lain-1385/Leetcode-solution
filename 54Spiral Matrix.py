class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        seen = set()
        direction = [(0,1),(1,0),(0,-1),(-1,0)]
        m = len(matrix)
        n = len(matrix[0])
        num_turn = 0
        cur_row, cur_column = (0,0)
        flag_turn = False
        res = [matrix[0][0]]
        seen.add((0,0))
        while True:
            cur_row = cur_row + direction[num_turn % 4][0]
            cur_column = cur_column + direction[num_turn % 4][1] 
            if cur_row < 0 or cur_row > m - 1 or cur_column < 0 or cur_column > n - 1 or (cur_row, cur_column) in seen:
                cur_row -= direction[num_turn % 4][0]
                cur_column -= direction[num_turn % 4][1]
                num_turn += 1
                if flag_turn == True:
                    break
                else:
                    flag_turn = True
                continue
            else:
                flag_turn = False
                seen.add((cur_row,cur_column))
                res.append(matrix[cur_row][cur_column])
        return res
    
# better
class Solution:
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        return ans