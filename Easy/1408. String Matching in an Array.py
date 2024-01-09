class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Brutal Force with Time Complexity O(n^3)
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and words[i] != words[j]:
                    res.append(words[i])
                    break
        return list(res)
