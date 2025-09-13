class Solution:
    def maxFreqSum(self, s: str) -> int:
        d = defaultdict(int)
        max_vowel = 0
        max_consonant = 0

        for i in s:
            d[i] += 1
            if i in 'aiueo':
                if d[i] > max_vowel:
                    max_vowel = d[i]
            else:
                if d[i] > max_consonant:
                    max_consonant = d[i]

        return max_vowel + max_consonant
