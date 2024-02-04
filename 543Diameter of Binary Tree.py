# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def depth(root: Optional[TreeNode]):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            res[0] = max(res[0], left + right)
            return 1 + max(left, right)
        depth(root)
        return res[0]


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def depth(root: Optional[TreeNode]):
            if not root:
                return 0 
            left = depth(root.left)
            right = depth(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        depth(root)
        return self.res
