# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return [0,0]
            leftTree=dfs(node.left)
            rightTree=dfs(node.right)
            includeCurrNode=node.val+leftTree[1]+rightTree[1]
            withoutCurrNode=max(leftTree)+max(rightTree)
            # print(node.val,[includeCurrNode, withoutCurrNode])
            return [includeCurrNode, withoutCurrNode]
        print(dfs(root))
        return max(dfs(root))        