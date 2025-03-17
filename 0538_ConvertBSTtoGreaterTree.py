# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root):
        self.s = 0
        def visit(root):
            if root:
                rootRight = visit(root.right)
                root.val += self.s
                self.s = root.val
                rootLeft = visit(root.left)
        visit(root)
        return root
