class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split()
        for i in range(len(s)):
            if s[i][0] not in 'aiueo':
                s[i] = s[i][1:] + s[i][0]
            s[i] = s[i] + 'ma'
            s[i] = s[i] + 'a' * i
        return ' '.join(s)
