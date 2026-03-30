class TrieNode:
    def __init__(self):
        self.children={}
        self.isEndOfWord=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.isEndOfWord=True


    def search(self, word: str) -> bool:
        def dfs(j,root):
            curr=root
            for i in range(j,len(word)):
                char=word[i]
                if char=='.':
                    #recursive
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                    #iterative
                    if char not in curr.children:
                        return False
                    curr=curr.children[char]
            return curr.isEndOfWord
        return dfs(0, self.root)
