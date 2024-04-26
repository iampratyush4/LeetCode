# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root ==None : return []
        result,Q=[],[]
        Q.append(root)
        while Q:
            count=len(Q)
            level_node=[]
            for i in range(count):
                node=Q[0]
                Q.pop(0)
                
                if node.right is not None: 
                    Q.append(node.right)

                if node.left is not None: 
                    Q.append(node.left)

                if node.left is None :
                    print(node.val,"this is node val" )
                    level_node.append(None)

                level_node.append(node.val)

                if node.right is None :
                    level_node.append(None)
            
                
            if level_node != list(reversed(level_node)):
                return False
            print(level_node)
            result.append(level_node)

            # print (level_node)
        return True
            



        

        

        