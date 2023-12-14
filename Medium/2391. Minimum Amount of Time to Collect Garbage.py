class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        sumPick = len(''.join(garbage))
        pre = [travel[0]]
        for i in range(1, len(travel)):
            pre.append(pre[-1] + travel[i])

        def findLast(garbage, type):
            for i in range(len(garbage) - 1, 0, -1):
                if type in garbage[i]:
                    return i - 1
            return -1

        def getTravelTime(type):
            check = findLast(garbage, type)
            return pre[check] if check != -1 else 0
        return sumPick + sum([getTravelTime(type) for type in ['M', 'G', 'P']])
