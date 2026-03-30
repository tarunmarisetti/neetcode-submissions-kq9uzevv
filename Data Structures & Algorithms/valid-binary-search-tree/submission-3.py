# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(min_val, node, max_val):
            if not node:
                return True
            if not min_val<node.val<max_val:
                return False
            return isValid(min_val,node.left, node.val) and isValid(node.val, node.right, max_val)
        return isValid(float('-inf'), root, float('inf'))
        