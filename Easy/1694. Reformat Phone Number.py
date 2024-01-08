import re


class Solution:
    def reformatNumber(self, number: str) -> str:
        sep = re.split('[ -]', number)
        number = ''.join(sep)
        lst = []
        i = 3
        while i <= len(number):
            lst.append(number[i - 3:i])
            if len(number) - i % 3 == 0:
                i += 3
            else:
                i += 2
        return '-'.join(lst)
