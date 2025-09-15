class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(' ')
        counter = 0
        for word in words:
            for c in word:
                if c in brokenLetters:
                    counter += 1
                    break

        return len(words) - counter
