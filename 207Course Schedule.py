'''
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        mydict = {}
        myset = set()
        for i in prerequisites:
            if i[0] in mydict:
                mydict[i[0]].append(i[1])   
            else:
                mydict[i[0]]= [i[1]]
        
        cur_class = prerequisites[0][0]
        while mydict:
            if cur_class in mydict:
                temp = mydict[cur_class][0]
                if len(mydict[cur_class]) == 1:
                    mydict.pop(cur_class)
                else:
                    mydict[cur_class].pop(0)
                if temp in myset or temp == cur_class:
                    return False
                else:
                    myset.add(cur_class)
                cur_class = temp
            else:
                myset.clear()
                cur_class = next(iter(mydict.items()))[0]
        return True
            
'''
from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegrees = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegrees[course] += 1

        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])

        while queue:
            prerequisite = queue.popleft()
            for course in graph[prerequisite]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)

        return sum(indegrees) == 0

# dfs
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            if visit[course] == -1:  # 如果正在访问中，说明找到了环
                return False
            if visit[course] == 1:  # 如果已经访问过，直接返回True
                return True
            visit[course] = -1  # 标记为正在访问
            for next_course in adj_list[course]:
                if not dfs(next_course):
                    return False
            visit[course] = 1  # 标记为已访问
            return True

        # 构建图的邻接列表
        adj_list = [[] for _ in range(numCourses)]
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        # 访问状态标记数组：0-未访问，-1-正在访问，1-已访问
        visit = [0] * numCourses

        # 对每个未访问的节点进行DFS遍历
        for i in range(numCourses):
            if visit[i] == 0 and not dfs(i):
                return False

        return True
