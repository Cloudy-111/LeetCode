from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        st = set()
        for i in dic:
            st.add(dic[i])
        return len(st) == len(dic)
