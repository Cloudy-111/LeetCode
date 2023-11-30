class Solution:
    def repeatedCharacter(self, s: str) -> str:
        lst = [] * 26
        for i in s:
            idx = ord(i) - ord('a')
            lst[idx] += 1
            if lst[idx] == 2:
                return i
