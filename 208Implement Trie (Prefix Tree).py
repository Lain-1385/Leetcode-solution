class Trie:

    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        cur = self.root
        for i in word:
            if i not in cur:
                cur[i] = {}
            cur = cur[i]
        cur['*'] = ''

    def search(self, word: str) -> bool:
        cur = self.root
        for i in word:
            if i not in cur:
                return False
            cur = cur[i]
        return '*' in cur  

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur:
                return False
            cur = cur[i]
        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)