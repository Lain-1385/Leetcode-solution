from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None:
            return []
        res = []
        temp = []
        cur_level = -1

        my_queue = deque()
        my_queue.append((root,0))
        while my_queue:
            node, new_level  = my_queue.popleft()
            if new_level != cur_level:
                cur_level = new_level
                res.append(temp)
                temp = []
            temp.append(node.val)
            if node.left:
                my_queue.append((node.left, new_level + 1))
            if node.right:
                my_queue.append((node.right, new_level + 1))
        res.append(temp)
        return res[1:]
    
# after optimization
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        res = []
        my_queue = deque()
        my_queue.append((root, 0))
        while my_queue:
            node, level = my_queue.popleft()
            if level == len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                my_queue.append((node.left, level + 1))
            if node.right:
                my_queue.append((node.right, level + 1))
        return res