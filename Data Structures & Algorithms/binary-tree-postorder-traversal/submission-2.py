# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # two stacks sol
        if not root:
            return []
        s1=[root]
        s2=[]
        res=[]
        while s1:
            node=s1.pop()
            s2.append(node)

            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:
            res.append(s2.pop().val)
        return res