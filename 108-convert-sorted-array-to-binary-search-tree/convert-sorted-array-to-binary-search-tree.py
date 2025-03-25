# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        # Special case: nums is empty.
        if not nums: 
            return None
        # Step 1: get the middle index
        middle_index = len(nums) // 2
        
        # Step 2: create a node that contains the value of the middle index.
        root = TreeNode(nums[middle_index])
        
        # Step 3: Use recursion to create the left and right sub-trees.
        root.left = self.sortedArrayToBST(nums[:middle_index]) # Create left subtree.
        root.right = self.sortedArrayToBST(nums[middle_index + 1:]) # Create right subtree.
        
        return root
        