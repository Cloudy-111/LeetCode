class Solution: # Use Replace function
    def maxDiff(self, num: int) -> int:
        max = self.turn_to_max(num)
        min = self.turn_to_min(num)
        return max - min
    
    def turn_to_max(self, num):  # Convert all digits with first digit other than 9 to 9
        s = str(num)
        for i in range(len(s)):
            if s[i] != '9':
                res = int(s.replace(s[i], '9'))
        else: res = num # If all digits are 9, return the original number
        return res  

    def turn_to_min(self, num):
        s = str(num)
        if s[0] != '1':
            return int(s.replace(s[0], '1'))    # If the first digit is not 1, change it to 1
        else:
            for i in range(1, len(s)):
                if s[i] not in '01':
                    res = int(s.replace(s[i], '0'))  # If the first digit is 1, change the first digit different from 1 to 0
                    break
            else:
                res = num   # If all digits are 1 or 0, return the original number
        return res

