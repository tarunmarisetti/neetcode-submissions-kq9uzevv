class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False

    def add(self,word):
        curr=self
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.is_end_of_word=True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r,c,node,word):
            if not(0<=r<rows) or not(0<=c<cols) or (r,c) in visited or board[r][c] not in node.children:
                return
            visited.add((r,c))
            node=node.children[board[r][c]]
            word+=board[r][c]
            if node.is_end_of_word:
                res.add(word)
            dfs(r+1,c,node,word)
            dfs(r-1,c,node,word)
            dfs(r,c+1,node,word)
            dfs(r,c-1,node,word)
            visited.remove((r,c))

        res=set()
        visited=set()
        root=TrieNode()
        for word in words:
            root.add(word)
        rows=len(board)
        cols=len(board[0])
        for row in range(rows):
            for col in range(cols):
                dfs(row,col,root,"")
        return list(res)
        