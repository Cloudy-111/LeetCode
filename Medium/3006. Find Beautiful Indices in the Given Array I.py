class Solution:
    # Bài này không khó, chỉ lâu ở chỗ làm sao cho lúc tìm số thỏa mãn có độ phức tạp thời gian là tối ưu nhất thôi
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        lstA, lstB = [], []
        for i in range(len(s)):  # O(n)
            if s[i: i + len(a)] == a:
                lstA.append(i)
            if s[i: i + len(b)] == b:
                lstB.append(i)
        if k > len(s) // 2:
            if len(lstA) and len(lstB):
                return lstA
            else:
                return []
        else:
            res = set()
            i, j = 0, 0
            while i < len(lstA) and j < len(lstB):  # O(n)
                if abs(lstA[i] - lstB[j]) <= k:
                    res.add(lstA[i])
                    i += 1
                else:
                    if lstA[i] > lstB[j]:
                        j += 1
                    else:
                        i += 1
            return sorted(list(res))  # O(nlogn)
