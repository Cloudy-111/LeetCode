class Solution:
    # Để tìm số mà XOR với num1 ra kết quả nhỏ nhất có nghĩa là tìm số có biểu diễn bit giống với num1 nhất
    # có nghĩa là ta sẽ điều chỉnh số lượng bit 1 trong biểu diễn bit của num1 sao cho bằng với số lượng bit 1 của num2
    def minimizeXor(self, num1: int, num2: int) -> int:
        # Đếm số lượng bit 1 trong biểu diễn bit của num1 và num2
        number_of_1_in_num1 = bin(num1).count('1')
        number_of_1_in_num2 = bin(num2).count('1')

        # Biểu diễn bit của num1
        # bit = list(bin(num1)[2:].zfill(32))
        bit = ['0'] * 32
        tmp = num1
        idx = 31
        while tmp > 0:
            if tmp % 2 == 1:
                bit[idx] = '1'
            idx -= 1
            tmp = tmp >> 1

        # Điều chỉnh số lượng bit 1 trong biểu diễn bit của num1 sao cho bằng với số lượng bit 1 của num2
        if number_of_1_in_num1 > number_of_1_in_num2:
            diff = number_of_1_in_num1 - number_of_1_in_num2
            for i in range(31, -1, -1):
                if bit[i] == '1':
                    bit[i] = '0'
                    diff -= 1
                    if diff == 0:
                        break
        elif number_of_1_in_num1 < number_of_1_in_num2:
            diff = number_of_1_in_num2 - number_of_1_in_num1
            for i in range(31, -1, -1):
                if bit[i] == '0':
                    bit[i] = '1'
                    diff -= 1
                    if diff == 0:
                        break
        return int(''.join(bit), 2)
