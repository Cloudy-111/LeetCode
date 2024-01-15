class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = {}
        loser = {}
        for i in matches:
            w, l = i
            if w in winner:
                winner[w] += 1
            else:
                winner[w] = 1
            if l in loser:
                loser[l] += 1
            else:
                loser[l] = 1
        res = []
        winAll = []
        winOne = []
        for i in winner:
            if i not in loser:
                winAll.append(i)
        for i in loser:
            if loser[i] == 1:
                winOne.append(i)
        res.append(sorted(winAll))
        res.append(sorted(winOne))
        return res
