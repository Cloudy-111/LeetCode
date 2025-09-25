class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        if numerator % denominator == 0:
            return str(numerator // denominator)

        numerator_abs = abs(numerator)
        denominator_abs = abs(denominator)

        int_part = int(numerator_abs / denominator_abs)
        modul = numerator_abs - int_part * denominator_abs
        if denominator_abs % 2 == 0 or denominator_abs % 5 == 0:
            for i in range(1000):
                if (10 ** i * modul) % denominator_abs == 0:
                    int_a = (10 ** i * modul) // denominator_abs
                    decimal_part = str(10 ** i + int_a)[1:]
                    return self.result(numerator, denominator, f"{int_part}.{decimal_part}")
            for i in range(1000):
                for j in range(1, 1000):
                    if (modul * 10 ** i * (10 ** j - 1)) % denominator_abs == 0:
                        int_b = ((modul * 10 ** i * (10 ** j - 1)) //
                                 denominator_abs) % (10 ** j - 1)
                        int_a = ((modul * 10 ** i * (10 ** j - 1)) //
                                 denominator_abs) // (10 ** j - 1)
                        if int_a <= 10 ** i and int_b <= 10 ** j and ((modul * 10 ** i * (10 ** j - 1)) // denominator_abs) - int_b == int_a * (10 ** i - 1):
                            decimal_part = str(
                                10 ** i + int_a)[1:] + "(" + str(10 ** j + int_b)[1:] + ")"
                            return self.result(numerator, denominator, f"{int_part}.{decimal_part}")
        else:
            i = 1
            while True:
                if (10 ** i - 1) % denominator_abs == 0:
                    decimal = modul * ((10 ** i - 1) // denominator_abs)
                    decimal_part = str(10 ** i + decimal)[1:]
                    break
                i += 1
            return self.result(numerator, denominator, f"{int_part}.({decimal_part})")

    def result(self, numerator, denominator, res):
        if numerator * denominator > 0:
            return res
        return "-" + res
