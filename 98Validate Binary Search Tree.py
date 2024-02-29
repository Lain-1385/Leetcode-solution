# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = True
        if root.left:
            if self.subtree_max(root.left) >= root.val:
                return False
            res = Solution.isValidBST(self, root.left)
        if root.right:
            if self.subtree_min(root.right) <= root.val:
                return False
            res = res and Solution.isValidBST(self, root.right)
        return res
    def subtree_min(self, root: Optional[TreeNode]):
            while root.left:
                root = root.left
            return root.val
    def subtree_max(self, root: Optional[TreeNode]):
            while root.right:
                root = root.right
            return root.val
    
# better version

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(node: Optional[TreeNode]):
            if node is None:
                return True, None, None
            right_is_bst, right_min, right_max = recursion(node.right)
            left_is_bst, left_min, left_max = recursion(node.left)
            
            if not right_is_bst or not left_is_bst:
                return False, None, None
            
            if node.right and node.val >= right_min:
                return False, None, None
            if node.left and node.val <= left_max:
                return False, None, None
            
            min_val = left_min if left_min is not None else node.val
            max_val = right_max if right_max is not None else node.val
            
            return True, min_val, max_val
        
        return recursion(root)[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val)
        
        return validate(root, float('-inf'), float('inf'))