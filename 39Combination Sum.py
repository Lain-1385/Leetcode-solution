from collections import deque
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
            candidates.sort()
            res = []
            bfs = deque()
            for i in candidates:
                bfs.append(([i], i))
            while bfs:
                cur_candiadates, cur_sum = bfs.popleft()
                last_added = cur_candiadates[-1]
                if cur_sum < target:
                    for i in candidates:
                        # only greater or equal to last added elements are permitted
                        if i >= last_added:
                            bfs.append((cur_candiadates+[i], cur_sum + i))
                        if cur_sum + i > target:
                            break
                elif cur_sum == target:
                    res.append(cur_candiadates)
            return res