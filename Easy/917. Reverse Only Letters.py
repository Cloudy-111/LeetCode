class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def isAlphabet(x):
            return 'a' <= x <= 'z' or 'A' <= x <= 'Z'
        l, r = 0, len(s) - 1
        lst = list(s)
        while l < r:
            if isAlphabet(lst[l]) and isAlphabet(lst[r]):
                lst[l], lst[r] = lst[r], lst[l]
                l += 1
                r -= 1
            else:
                if not isAlphabet(lst[l]):
                    l += 1
                if not isAlphabet(lst[r]):
                    r -= 1
        return ''.join(lst)
