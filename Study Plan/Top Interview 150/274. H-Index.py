from collections import Counter

#


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        freq = Counter(citations)
        pref = [0]
        for key in sorted(freq.keys(), reverse=True):
            pref.append(pref[-1] + freq[key])
        i = 1
        res = 0
        for key in sorted(freq.keys(), reverse=True):
            res = max(res, min(key, pref[i]))
            i += 1
        return res
