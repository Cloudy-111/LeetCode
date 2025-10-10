class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)
        rev = energy[::-1]

        for i in range(k, n):
            rev[i] = rev[i] + rev[i - k]

        res = float("-inf")
        for i in range(n):
            res = max(res, rev[i])

        return res


# Can abbreviated as:

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        n = len(energy)

        res = float("-inf")
        for i in range(n - 1, -1, -1):
            if i < n - k:
                energy[i] = energy[i] + energy[i + k]
            res = max(res, energy[i])

        return res
