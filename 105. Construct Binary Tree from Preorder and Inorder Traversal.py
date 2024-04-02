# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        cur = TreeNode(-1)
        result = cur
        def recursion(p, i, isleft, cur):
            if not p:
                return None
            node = TreeNode(p[0])
            if isleft:
                cur.left = node
            else:
                cur.right = node
            # process left subtree
            idx =  i.index(p[0])
            cur = node
            recursion(p[1:idx +1], i[0 : idx], True, cur)
            # process right subtree
            recursion(p[idx + 1:], i[idx+1 : ], False, cur)
        recursion(preorder, inorder, True, cur)
        return result.left
    

class Solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root

class Solution:
    def buildTree(self, preorder, inorder):
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def helper(preorder_left, preorder_right, inorder_left, inorder_right):
            if preorder_left > preorder_right:
                return None

            preorder_root = preorder_left
            inorder_root = inorder_map[preorder[preorder_root]]

            root = TreeNode(preorder[preorder_root])
            size_left_subtree = inorder_root - inorder_left

            root.left = helper(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            root.right = helper(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)

            return root

        n = len(preorder)
        return helper(0, n - 1, 0, n - 1)