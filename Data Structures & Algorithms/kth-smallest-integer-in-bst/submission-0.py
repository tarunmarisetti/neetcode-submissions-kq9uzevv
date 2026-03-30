# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.pos=0
        self.res=None
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            self.pos+=1
            if self.pos==k:
                self.res=node.val
                return
            inorder(node.right)
        inorder(root)
        return self.res
