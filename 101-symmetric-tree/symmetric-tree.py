# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:


        def checkdfs(left,right):

            if not left and not right:
                return True
            if not left or not right:
                return False
            ans= (left.val == right.val and checkdfs(left.left,right.right) and checkdfs(left.right, right.left))
                    
            return ans
        return checkdfs(root.left,root.right)




        

        

        