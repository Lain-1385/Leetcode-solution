from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        flag_left = -1
        flag_right = -1
        for index, i in enumerate(intervals):
            # split into 4 situation
            if i[0] <= newInterval[0] and i[1] >= newInterval[0]:
                flag_left = index
            if i[0] <= newInterval[1] and i[1] >= newInterval[1]:
                flag_right = index
        if flag_left == -1 and flag_right == -1:
            left = Solution.left_position(intervals, newInterval)
            right = Solution.right_position(intervals, newInterval) 
            # delete certain elements by order of List[][0] and List[][1]
            del intervals[left: right]
            intervals.insert(left, newInterval)
        elif flag_left != -1 and flag_right == -1:
            new = [intervals[flag_left][0], newInterval[1]]
            del intervals[flag_left]
            left = Solution.left_position(intervals, new)
            right = Solution.right_position(intervals, newInterval) 
            del intervals[left: right]
            intervals.insert(left, new)
        elif flag_left == -1 and flag_right != -1:
            new = [newInterval[0], intervals[flag_right][1]]
            del intervals[flag_right]
            left = Solution.left_position(intervals, new)
            right = Solution.right_position(intervals, newInterval) 
            del intervals[left: right]
            intervals.insert(left, new)
        elif flag_left != -1 and flag_right != -1:
            temp = [intervals[flag_left][0],intervals[flag_right][1]]
            del intervals[flag_left: flag_right + 1]
            intervals.insert(flag_left,temp)
        return intervals
    
    def left_position(intervals: List[List[int]], newInterval: List[int]):
        # after add newInterval into intervals and sort by intervals[][0], return the index of newInterval
        for index, i in enumerate(intervals):
            if i[0] > newInterval[0]:
                return index
        return len(intervals)
    
    def right_position(intervals: List[List[int]], newInterval: List[int]):
        # after add newInterval into intervals and sort by intervals[][1], return the index of newInterval
        for index, i in enumerate(intervals):
            if i[1] > newInterval[1]:
                return index
        return len(intervals)
    
s = Solution()
a = [[1,5]]

b = [6,8]
print(s.insert(a,b))