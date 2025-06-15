class Solution:
    def maxDiff(self, num: int) -> int:
        if num < 10: return 8
        max = self.turn_to_max(num)
        min = self.turn_to_min(num)
        print(max, min)
        return max - min

    def turn_to_max(self, num): # Convert all digits with first digit other than 9 to 9
        s = str(num)
        res = ""
        mark = -1
        for i in range(len(s)):
            if s[i] != '9':
                mark = s[i]
                break
        for i in range(len(s)):
            if s[i] == mark:
                res += '9'
            else: res += s[i]
        return int(res)
    
    def turn_to_min(self, num):
        s = str(num)
        d = Counter(s)
        if d[s[0]] == len(s): return int("1" * len(s)) # If all digits are the same, return a number with all digits as 1
        idx = -1
        for i in range(len(s)):
            if s[i] != "1" and s[i] != "0":
                idx = i
                break
        if idx == -1: return num # If all digits are 1 or 0, return the original number
        if len(d) == 2: 
            if d["0"] != 0:
                res = ""
                for i in range(len(s)):
                    if s[i] != "0":
                        res += "1"
                    else: res += "0"
                return int(res) # If there are two digits, and one of them is 0, return a number with all digits as 1 except 0
        res = ""
        mark = "-1"
        if s[0] == "1": 
            i = 0
            while s[i] == "1" or s[i] == "0": 
                i += 1
            mark = s[i]
        else:
            mark = s[0]
        res += "1"
        for i in range(1, len(s)):
            if s[i] == mark:
                if mark == s[0]: res += "1"
                else: res += "0"
            else: res += s[i]
        return int(res) # If there are more than two digits, change the first digit to 1, if the first digit is equal to 1, change the first digit different from 1 to 0
