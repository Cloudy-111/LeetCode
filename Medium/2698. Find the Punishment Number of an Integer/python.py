def is_valid_split(square_str, target, index=0, current_sum=0):
    """Dùng backtracking kiểm tra xem có thể tách square_str để tổng bằng target."""
    if index == len(square_str):
        return current_sum == target  # Nếu đã xét hết và tổng đúng, trả về True

    num = 0
    for i in range(index, len(square_str)):
        num = num * 10 + int(square_str[i])  # Xây dựng số từng phần

        if num + current_sum > target:  # Cắt nhánh nếu tổng vượt quá target
            return False

        if is_valid_split(square_str, target, i + 1, current_sum + num):
            return True

    return False


def find_optimized_special_numbers(limit):
    special_numbers = []

    for n in range(1, limit + 1):
        square_str = str(n ** 2)  # Bình phương của n dưới dạng chuỗi
        # Kiểm tra xem có thể chia thành tổng bằng n không
        if is_valid_split(square_str, n):
            special_numbers.append(n)

    return special_numbers


# Tìm các số thỏa mãn yêu cầu trong khoảng <= 1000
optimized_special_numbers = find_optimized_special_numbers(1000)
print(optimized_special_numbers)
