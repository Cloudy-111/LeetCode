class Solution:
    # Đơn giản chỉ cần tạo mảng pref để lưu prefixsum của số lượng chuỗi có chứa nguyên âm ở đầu và cuối từ 0 đến i
    # Những dạng bài queries left right thì ta dùng prefixsum để giảm độ phức tạp của bài toán
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        pref = [0]
        for i in range(len(words)):
            if words[i][-1] in 'aeiou' and words[i][0] in 'aeiou':
                pref.append(pref[-1] + 1)
            else:
                pref.append(pref[-1])
        res = []
        for l, r in queries:
            res.append(pref[r + 1] - pref[l])
        return res
