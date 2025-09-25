class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        res = []
        if numerator == 0:
            return "0"
        if numerator % denominator == 0:
            return str(numerator // denominator)
        if numerator * denominator < 0:
            res.append('-')

        n, d = abs(numerator), abs(denominator)
        res.append(str(n // d))
        res.append('.')
        modul = n % d
        dic = {}
        while modul != 0 and modul not in dic:
            dic[modul] = len(res)
            modul *= 10
            res.append(str(modul // d))
            modul = modul % d
        if modul in dic:
            res.insert(dic[modul], '(')
            res.append(')')
            return ''.join(res)
        return ''.join(res)
