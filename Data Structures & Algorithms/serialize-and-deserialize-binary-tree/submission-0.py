# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        node_val=[]
        def dfs(root):
            if not root:
                node_val.append("N")
                return
            node_val.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(node_val)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes=data.split(',')
        self.index=0
        def dfs():
            if nodes[self.index]=="N":
                self.index+=1
                return None
            root=TreeNode(int(nodes[self.index]))
            self.index+=1
            root.left=dfs()
            root.right=dfs()
            return root
        return dfs()
