class Solution:
    def checkString(self, s: str) -> bool:
        idxB = s.find('b')
        if idxB == -1:
            return True
        if 'a' in s[idxB:]:
            return False
        return True
