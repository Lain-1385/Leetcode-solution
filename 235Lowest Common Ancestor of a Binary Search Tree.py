# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        def Traverse_B(root: 'Treenode'):
            stack.append(root)
            if root.left:
                Traverse(root.left)
            if root.right:
                Traverse(root.right)
        def find(root: 'TreeNode', p: 'TreeNode'):
            if root == p:
                return True
            elif root.left == None and root.right == None:
                return False
            if root.val > p.val and root.left:
                return find(root.left,p)
            if root.val < p.val and root.right:
                return find(root.right,p)
        Traverse(root)
        temp = root
        while stack:
            temp = stack.pop()
            if find(temp, p) and find(temp, q):
                return temp
        return root

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root