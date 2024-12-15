from collections import Counter


def countKeyChanges(s):
    s = s.lower()
    res = 0
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            res += 1
    return res
