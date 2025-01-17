class Solution:
    # Dùng XOR để tìm lại mảng gốc từ mảng đã cho
    # Tận dụng tính chất của XOR: a XOR a = 0 và a XOR 0 = a
    # Mảng derived được tạo ra từ derived[i] = original[i] XOR original[i + 1] -> khi XOR hết mảng derived thì phải = 0
    # Nên nếu mảng derived có số lượng số 1 là chẵn thì chắc chắn sẽ tạo lại được mảng gốc
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        return sum(derived) % 2 == 0
