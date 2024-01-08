class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split()

        def checkPrefix(word, check):
            if len(word) < len(check):
                return False
            i = 0
            while i < len(check):
                if word[i] != check[i]:
                    return False
                i += 1
            return True
        for i in range(len(words)):
            # if words[i].startswith(searchWord): return i + 1
            if checkPrefix(words[i], searchWord):
                return i + 1
        return -1
