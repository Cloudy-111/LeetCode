class Solution:
    # khi các xâu trong list đều bằng nhau thì các số lần xuất hiện của mỗi kí tự phải đều chia hết cho độ dài list
    def makeEqual(self, words: List[str]) -> bool:
        dic = {}
        if len(words) == 1:
            return True
        for i in words:
            for j in i:
                if j not in dic:
                    dic[j] = 1
                else:
                    dic[j] += 1
        for i in dic:
            if dic[i] % len(words) != 0:
                return False
        return True
