from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        dic = Counter(chars)
        res = 0
        for word in words:
            wordCount = Counter(word)
            chk = 0
            for i, freq in wordCount.items():
                if freq > dic[i]:
                    chk = 1
                    break
            if chk == 0:
                res += len(word)
        return res
