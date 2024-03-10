# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        def Traverse(root: 'Treenode'):
            stack.append(root)
            if root.left:
                Traverse(root.left)
            if root.right:
                Traverse(root.right)
        def find(root: 'TreeNode', p: 'TreeNode'):
            if root == None:
                return False
            if root == p:
                return True
            else:
                return find(root.left, p) or find(root.right, p)
        Traverse(root)
        temp = root
        while stack:
            temp = stack.pop()
            if find(temp, p) and find(temp, q):
                return temp


# better
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if root is None or root is one of the targets (p or q),
        # return root as the LCA (or as part of the path to the LCA).
        if not root or root == p or root == q:
            return root
        
        # Search for targets in the left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both left and right are non-null, it means we have found the two targets in 
        # the left and right subtrees of the current root. Hence, root is the LCA.
        if left and right:
            return root
        
        # If one of the subtrees returns a node (either p or q), it means that is the current LCA.
        # Otherwise, return whichever subtree is non-null, propagating the found target node (or None) upwards.
        return left or right