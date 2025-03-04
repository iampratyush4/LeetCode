# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         # Assign the value of the node.
#         self.val = val
#         # Pointer/reference to the left child node.
#         self.left = left
#         # Pointer/reference to the right child node.
#         self.right = right

class Solution:
    def isBalanced(self, root):

        def dfs(node):
            # Base case: if the node is None, it is considered balanced with height 0.
            if not node:
                return [True, 0]
            
            left = dfs(node.left) # Recursively get balance info and height from the left subtree.

            right = dfs(node.right) # Recursively get balance info and height from the right subtree.
            # A subtree is balanced if:
            # 1) The left subtree is balanced, 2) The right subtree is balanced, and The absolute difference in heights of left and right subtree <= 1.
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # Height of the current subtree is:
            height = 1 + max(left[1], right[1])# 1 (for the current node) + the max of left and right subtree heights.
            return [balanced, height] # Return both whether it's balanced and its height.
        # Call the dfs function on the root. The dfs returns [is_balanced, height].
        return dfs(root)[0] # We only need the 'is_balanced' part for the final answer, so we return dfs(root)[0].
