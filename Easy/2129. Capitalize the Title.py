class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.title().split()
        for i in range(len(words)):
            if len(words[i]) < 3:
                words[i] = words[i].lower()
        return ' '.join(words)
