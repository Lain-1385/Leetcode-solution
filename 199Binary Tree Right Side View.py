# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        stack = []
        stack.append((0, root))
        res = []
        seen = set()
        while stack:
            cur_depth, cur_node = stack.pop()
            if not cur_depth in seen:
                res.append(cur_node.val)
                seen.add(cur_depth)
            if cur_node.left:
                stack.append((cur_depth + 1, cur_node.left))
            if cur_node.right:
                stack.append((cur_depth + 1, cur_node.right))
        return res
#better
class Solution:
    def rightSideView(self, root):
        if root is None:
            return []
        stack = [(root, 0)]
        res = []
        while stack:
            node, depth = stack.pop()
            if depth == len(res):
                res.append(node.val)
            if node.left:
                stack.append((node.left, depth + 1))
            if node.right:
                stack.append((node.right, depth + 1))
        return res