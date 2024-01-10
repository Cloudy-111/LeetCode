class Solution:
    # lấy ra >= 2 số trong mảng sao cho OR với nhau thì có biểu diển bit kết thúc là số 0
    # chỉ có 0 OR 0 = 0 nên trong mảng chỉ cần có 2 số chẵn(có biểu diễn bit kết thúc là số 0) là thỏa mãn yêu cầu
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        even_num = 0
        for i in nums:
            if i % 2 == 0:
                even_num += 1
        if even_num >= 2:
            return True
        return False
