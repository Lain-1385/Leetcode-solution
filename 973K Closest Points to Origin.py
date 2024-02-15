'''
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for i in points:
            distance = self.distance(i)
            distances.append((distance,i))
        distances.sort(key = lambda x:x[0])
        return [point for _, point in distances[:k]]
        
    
    def distance(self,point: List[int]):
        return math.sqrt(point[0] ** 2 + point[1] ** 2)
'''

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap =[]
        for (x, y) in points:
            dist = -(x**2 + y**2)
            if len(maxHeap) < k:
                heapq.heappush(maxHeap, (dist,x,y))
            elif dist > maxHeap[0][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap,(dist,x,y))
        return [(x,y) for (dist,x,y) in maxHeap]
