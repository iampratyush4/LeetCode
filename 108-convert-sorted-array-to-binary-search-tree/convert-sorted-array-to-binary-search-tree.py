# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def midnode(l,r):
            if l>r:
                return None
            m=(l+r)//2
            root= TreeNode(nums[m])
            root.left=midnode(l,m-1)
            root.right=midnode(m+1,r)
            return root
        return midnode(0,len(nums)-1)
