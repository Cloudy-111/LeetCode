class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        res = ""
        for i in range(len(s)):
            res += s[i]
            if len(res) >= len(part) and res[len(res) - len(part):] == part:
                res = res[:len(res) - len(part)]
        return res

        # while part in s:
        #     s = s.replace(part, "", 1)
        # return s
