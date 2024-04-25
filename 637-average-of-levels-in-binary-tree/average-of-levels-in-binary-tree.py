# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import numpy
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if root ==None : return []
        result,Q=[],[]
        Q.append(root)
        while Q:
            count=len(Q)
            level_node=[]
            for i in range(count):
                node=Q[0]
                Q.pop(0)
                if node.left is not None: 
                    Q.append(node.left)
                if node.right is not None: 
                    Q.append(node.right)
                level_node.append(node.val)
            result.append(numpy.average(level_node))
        return result

        