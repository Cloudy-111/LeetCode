class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(x):
            return x in 'aeiouAEIOU'
        lst = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            if isVowel(lst[l]) and isVowel(lst[r]):
                lst[l], lst[r] = lst[r], lst[l]
            elif isVowel(lst[l]):
                r -= 1
            elif isVowel(lst[r]):
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(lst)
