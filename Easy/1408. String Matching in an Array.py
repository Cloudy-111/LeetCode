class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Brutal Force with Time Complexity O(n^3)
        res = []
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and words[i] != words[j]:
                    res.append(words[i])
                    break
        return list(res)

# Time Complexity: O(k * N) với k là tổng số lượng từ ; N là tổng số lượng kí tự trong mảng


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        total_string = ' '.join(words)
        res = [s for s in words if total_string.count(s) > 1]
        return res
