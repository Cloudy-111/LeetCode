class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for i in range(len(s)):
            if s[i] in 'aiueo':
                return True
        return False