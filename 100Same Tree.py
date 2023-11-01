# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # exclude the case where there are none, to make sure p and q are not None
        if p == None or q == None:
            if p == None and q == None:
                return True
            else:
                return False
        
        # when p and q are not None, if val is not same, it will be false
        if p.val != q.val:
            return False

        # judge left tree and right tree
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)