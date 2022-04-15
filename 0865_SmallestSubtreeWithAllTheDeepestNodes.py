class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findSubTreeRecursively(root, length = 0):
    if not root:
        return {"length": length, "node": root}
    while(root):
        leftRes = findSubTreeRecursively(root.left, length + 1)
        rightRes = findSubTreeRecursively(root.right, length + 1)

        if leftRes["length"] == rightRes["length"]:
            return {"length": leftRes["length"], "node": root}
        elif leftRes["length"] > rightRes["length"]:
                return {"length": leftRes["length"], "node": leftRes["node"]}
        elif leftRes["length"] < rightRes["length"]:
                return {"length": rightRes["length"], "node": rightRes["node"]}

class Solution:        
    def subtreeWithAllDeepest(self, root):
        if not root:
            return None
        result = findSubTreeRecursively(root)
        print(result)
        return result["node"]
