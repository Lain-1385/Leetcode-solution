class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key = lambda x: (x[0]))
        last_end = -1

        for interval in intervals:
            if interval[0] > last_end:
                res.append(interval)
                last_end = interval[1]
            else:
                res[-1][1] = max(interval[1], res[-1][1])
                last_end = res[-1][1]
        return res
