# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(leftNode, node,rightNode):
            if not node:
                return True
            if not leftNode<node.val<rightNode:
                return False
            return dfs(leftNode, node.left, node.val) and  dfs(node.val, node.right, rightNode)
        
        return dfs(float('-inf'), root, float('inf'))
        