class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0]) # m is row, n is colomn
        res = [[-1]* n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                    if mat[i][j] == 0:
                        res[i][j] = 0
                    else:
                        temp = min(res[i-1][j] if i > 0 else 9999
                                , res[i][j-1] if j > 0 else 9999
                                ) + 1
                        res[i][j] = temp
        for i in range(m-1, -1 ,-1):
            for j in range(n-1, -1, -1):
                    if mat[i][j] != 0:
                        temp = min(res[i+1][j] if i < m - 1 else 9999
                                , res[i][j+1] if j < n - 1 else 9999
                                ) + 1
                        res[i][j] = temp
        return res
                        
