# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def depth(root: Optional[TreeNode]):
            if not root:
                return 0
            else:
                return max(1+depth(root.left), 1+depth(root.right))
        depth_sub = depth(root.left) - depth(root.right)
        if depth_sub < 2 and depth_sub > -2:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
'''better version'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def depth(root: Optional[TreeNode]):
            if not root:
                return 0
            left = depth(root.left)
            right = depth(root.right)
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1
            return max(left, right) + 1
        return depth(root) != -1