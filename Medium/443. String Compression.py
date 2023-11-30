class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append('..')
        lst = []
        count = 1
        for i in range(1, len(chars)):
            if chars[i] != chars[i - 1]:
                lst.append(chars[i - 1])
                if count > 1:
                    lst = lst + list(str(count))
                count = 1
            else:
                count += 1
        for i in range(len(lst)):
            chars[i] = lst[i]
        return len(lst)
