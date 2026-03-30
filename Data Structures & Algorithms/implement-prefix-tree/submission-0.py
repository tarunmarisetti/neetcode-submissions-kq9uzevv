class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end_of_word=False

class PrefixTree:

    def __init__(self):
        self.Trie=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.Trie
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.is_end_of_word=True

    def search(self, word: str) -> bool:
        curr=self.Trie
        for char in word:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        return curr.is_end_of_word


    def startsWith(self, prefix: str) -> bool:
        curr=self.Trie
        for char in prefix:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        return True
        
        