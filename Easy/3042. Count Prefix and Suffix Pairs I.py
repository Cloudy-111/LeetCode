# Cách 1: Brute Force, chỉ cần duyệt tất cả các cặp j i với j < i mà thỏa mãn
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0
        for i in range(len(words)):
            for j in range(i):
                if len(words[j]) > len(words[i]):
                    continue
                if words[i].startswith(words[j]) and words[i].endswith(words[j]):
                    res += 1
        return res

# Cách 2: Sử dụng Trie để lưu trữ tiền tố và hậu tố của từ


class Node:
    def __init__(self):
        self.link_tree = [None] * 26

    def _contains(self, c) -> bool:
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

    def isPrefix(self, word: str) -> bool:
        node = self.root
        for char in word:
            if not node._contains(char):
                return False
            node = node._next(char)
        return True


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        res = 0

        for i in range(len(words)):
            word = words[i]
            rev_word = word[::-1]

            prefix_trie = Trie()
            suffix_trie = Trie()

            prefix_trie.insert(word)
            suffix_trie.insert(rev_word)

            for j in range(i):
                if len(words[j]) > len(word):
                    pass
                if prefix_trie.isPrefix(word) and suffix_trie.isPrefix(rev_word):
                    res += 1
        return res
