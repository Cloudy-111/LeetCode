class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_s = []
        s_t = []
        for i in range(len(s)):
            if len(s_s) > 0 and s[i] == '#':
                s_s.pop()
            if s[i] != '#': s_s.append(s[i])
        # print(''.join(s_s))

        for i in range(len(t)):
            if len(s_t) > 0 and t[i] == '#':
                s_t.pop()
            if t[i] != '#': s_t.append(t[i])
        # print(''.join(s_t))
        return ''.join(s_s) == ''.join(s_t)