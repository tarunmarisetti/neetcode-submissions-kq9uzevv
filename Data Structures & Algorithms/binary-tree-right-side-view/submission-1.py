# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_side_view=[]
        q=deque([root])
        while q:
            q_len=len(q)
            for i in range(q_len):
                node=q.popleft()
                if i==q_len-1:
                    right_side_view.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return right_side_view
            

        