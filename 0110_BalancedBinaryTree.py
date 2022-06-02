class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBBT(self, root, height=1):
        if not root:
            return height
        leftHeight = self.isBBT(root.left, height+1)
        rightHeight = self.isBBT(root.right, height+1)
        
        if leftHeight and rightHeight and abs(leftHeight - rightHeight) <= 1:
            return max(leftHeight, rightHeight)

        return False


    def isBalanced(self, root):
        return True if self.isBBT(root, height=1) else False

