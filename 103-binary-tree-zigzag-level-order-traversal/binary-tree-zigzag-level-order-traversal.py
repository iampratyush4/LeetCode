# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root ==None : return []
        result,Q=[],[]
        Q.append(root)
        c=0
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

            if c%2 ==0:
                result.append(level_node)
                c=c+1

            else:

                result.append(reversed(level_node))
                c=c+1
        return result
