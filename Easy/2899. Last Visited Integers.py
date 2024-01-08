class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        res = []
        tmp = []
        k = 0
        for i in range(len(words)):
            if words[i] != 'prev':
                tmp.append(int(words[i]))
                k = len(tmp)
            else:
                if k > 0:
                    res.append(tmp[k - 1])
                    k -= 1
                else:
                    res.append(-1)
        return res
