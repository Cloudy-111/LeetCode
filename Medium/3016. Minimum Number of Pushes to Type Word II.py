class Solution:
    def minimumPushes(self, word: str) -> int:
        letter = [0 for _ in range(26)]
        for i in word:
            letter[ord(i) - 97] += 1
        freq = sorted([x for x in letter if x != 0], reverse=True)
        div = len(freq) // 8
        res = 0
        for i in range(1, div + 1):
            res += sum(freq[8 * (i - 1): 8 * i]) * i
        return res + sum(freq[8 * div:]) * (div + 1)
