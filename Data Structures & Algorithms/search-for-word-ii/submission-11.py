class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False

    def addWord(self,word):
        curr=self
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.isEndOfWord=True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(r,c,curr, word):
            if not(0<=r<rows) or not(0<=c<cols) or (r,c) in visited or board[r][c] not in curr.children:
                return
            
            visited.add((r,c))
            curr=curr.children[board[r][c]]
            word+=board[r][c]
            if curr.isEndOfWord:
                res.add(word)
            dfs(r+1,c, curr, word)
            dfs(r,c+1, curr, word)
            dfs(r-1,c, curr, word)
            dfs(r,c-1, curr, word)
            visited.remove((r,c))


        rows=len(board)
        cols=len(board[0])
        visited=set()

        root=TrieNode()
        for word in words:
            root.addWord(word)
        
        res=set()
        for row in range(rows):
            for col in range(cols):
                dfs(row, col, root,"")
        return list(res)
        

        