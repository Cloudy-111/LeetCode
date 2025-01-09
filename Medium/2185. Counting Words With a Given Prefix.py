class Node:
    def __init__(self):
        self.link_tree = [None] * 26

    def _contains(self, c: str) -> bool:
        return self.link_tree[ord(c) - ord('a')] is not None

    def _add(self, c: str, node: "Node") -> None:
        self.link_tree[ord(c) - ord('a')] = node

    def _next(self, c: str) -> "Node":
        return self.link_tree[ord(c) - ord('a')]


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if not node._contains(char):
                node._add(char, Node())
            node = node._next(char)

    def isPrefix(self, pref: str) -> bool:
        node = self.root
        for char in pref:
            if not node._contains(char):
                return False
            node = node._next(char)
        return True


class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        res = 0
        for word in words:
            # if word.startswith(pref):
            #     res += 1
            prefix = Trie()
            prefix.insert(word)
            if prefix.isPrefix(pref):
                res += 1
        return res
