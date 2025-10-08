class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for i in range(len(spells)):
            target = success / spells[i]
            index = self.boundary_left(potions, target)
            res.append(len(potions) - index)
        return res

    def boundary_left(self, potions, target):
        l, r = 0, len(potions)
        while l < r:
            mid = (l + r) // 2
            if potions[mid] < target:
                l = mid + 1
            else:
                r = mid
        return l