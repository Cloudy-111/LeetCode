class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        res = 0
        if n == 0:
            return True
        for i in range(0, len(flowerbed)):
            if i == 0:
                if flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    res += 1
                    flowerbed[i] = 1
            elif i == len(flowerbed) - 1:
                if flowerbed[i - 1] == 0 and flowerbed[i] == 0:
                    res += 1
                    flowerbed[i] = 1
            else:
                if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0 and flowerbed[i] == 0:
                    res += 1
                    flowerbed[i] = 1
        return res >= n
