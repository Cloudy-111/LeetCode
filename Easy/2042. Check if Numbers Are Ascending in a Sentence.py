class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        chk = -1
        for i in s.split():
            if i.isdigit():
                if int(i) > chk:
                    chk = int(i)
                else:
                    return False
        return True
