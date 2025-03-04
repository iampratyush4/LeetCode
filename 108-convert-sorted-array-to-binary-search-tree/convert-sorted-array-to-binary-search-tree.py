# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val        # The value of the node.
#         self.left = left      # Pointer to the left child node.
#         self.right = right    # Pointer to the right child node.

# Solution class which implements the method to convert a sorted array to a balanced binary search tree.
class Solution:
    # Function to convert a sorted array into a Binary Search Tree (BST).
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Helper function to recursively find the middle of the array (or subarray)
        # and create the tree.
        def midnode(l, r):
            if l > r:        # Base case: if the left index exceeds the right index, return None.
                return None
            m = (l + r) // 2 # Find the middle index.
            root = TreeNode(nums[m])  # Create a new TreeNode with the middle element as its value.
            root.left = midnode(l, m - 1)  # Recursively construct the left subtree (left part of array).
            root.right = midnode(m + 1, r)  # Recursively construct the right subtree (right part of array).
            return root       # Return the created node with left and right children.

        return midnode(0, len(nums) - 1)  # Start the recursion with the entire array range.
