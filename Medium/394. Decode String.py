class Solution:
    def decodeString(self, s: str) -> str:
        res = []
        num = ''
        for i in s:
            if '0' <= i <= '9':
                num += i
            elif i == '[':
                res.append(int(num))
                num = ''
                res.append(i)
            elif 'a' <= i <= 'z':
                res.append(i)
            elif i == ']':
                print(res)
                tmp = ''
                while res[-1] != '[':
                    tmp = res.pop() + tmp
                res.pop()
                st = res.pop() * tmp
                res.append(st)
        return ''.join(res)
