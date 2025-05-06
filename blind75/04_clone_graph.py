from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return node
        
        cloned = {node.val: Node(node.val, [])}

        temp = list([node])
        
        while len(temp) > 0:
            item = temp.pop(0)
            curr_clone = cloned[item.val]

            for ngbr in item.neighbors:
                if ngbr.val not in cloned:
                    cloned[ngbr.val] = Node(ngbr.val, [])
                    temp.append(ngbr)
                
                curr_clone.neighbors.append(cloned[ngbr.val])

        return cloned[node.val]
