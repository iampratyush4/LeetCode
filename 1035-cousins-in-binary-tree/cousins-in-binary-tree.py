# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
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
                if node.left is not None and node.right is not None:

                    if  (node.left.val == x and node.right.val == y ) or ( node.left.val == y and node.right.val == x):
                        return False

                    

                if node.left is not None: 
                    Q.append(node.left)

                if node.right is not None: 
                    Q.append(node.right)
                
                    
                level_node.append(node.val)
            
            if x in level_node:
                if y in level_node:
                    print(x,y)
                    print(level_node)
                    return True

                
            
            result.append(level_node)
               
        print(result)
        return False



        
        