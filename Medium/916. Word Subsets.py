from collections import Counter


class Solution:
    # Đếm số lượng các kí tự max trong mỗi xâu của words2 và cho vào 1 dict
    # Với mỗi xâu thuộc words1, đếm số lượng kí tự trong dict đã có ở trên trong xâu đó và so sánh với nhau,
    # nếu kí tự nào trong xâu của words1 mà ít hơn kí tự trong dict thì loại bỏ xâu đó
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counter2 = dict()
        res = []
        for word in words2:
            counter = Counter(word)
            for char in word:
                counter2[char] = max(counter2.get(char, 0), counter[char])
        for word in words1:
            counter = Counter(word)
            check = 0
            for char in counter2:
                if counter2[char] > counter[char]:
                    check = 1
                    break
            if check == 0:
                res.append(word)
        return res
