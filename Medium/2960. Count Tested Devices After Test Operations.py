class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        res = 0
        cnt = 0
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] - cnt > 0:
                res += 1
                cnt += 1
        return res
