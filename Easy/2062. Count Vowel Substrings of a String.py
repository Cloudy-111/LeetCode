class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = 'aeiou'
        vowel_idx = {}
        start = 0
        res = 0
        for idx, x in enumerate(word):
            if x in vowels:
                if not vowel_idx:  # nếu dict rỗng thì set vị trí bắt đầu của chuỗi con
                    start = idx
                vowel_idx[x] = idx  # đặt vị trí mới nhất của kí tự x nguyên âm
                if len(vowel_idx) == 5:  # khi nào đủ 5 nguyên âm thì cộng
                    # mỗi lần đủ 5 nguyên âm thì cộng số lượng chuỗi con thỏa mãn đến vị trí đó
                    # khi viết ra, với mỗi lần đủ 5 nguyên âm thì số lượng chuỗi con mới mà thỏa mãn = vị trí nhỏ nhất của nguyên âm - vị trí bắt đầu của nguyên âm
                    res += min(vowel_idx.values()) - start + 1
            else:  # là phụ âm thì đặt lại dict
                vowel_idx.clear()
        return res
