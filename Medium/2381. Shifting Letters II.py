class Solution:
    # Bài này, thoạt nhìn thì thầy ngay cách làm: Chỉ cần cộng dồn mỗi khoảng của mảng shifts thì sẽ được total_shift
    # Sau đó, chỉ cần cộng dồn từng ký tự của s với total_shift tương ứng
    # Nhưng làm cách đó thì có vấn đề về Time Complexcity là O(n^2) vì phải duyệt start -> end trong mỗi phần tử của mảng shifts
    # Có thể rút gọn lại bằng tư duy sau:
    # Khi ta cần thay đổi 1 khoảng cùng 1 giá trị thì ta chỉ cần cộng dồn giá trị đó vào phần tử đầu tiên của khoảng và trừ giá trị đó vào phần tử cuối cùng của khoảng, gọi là mảng prefix_shift
    # Tức là mảng prefix_shift cho biết ta bắt đầu và kết thúc thay đổi tại những đâu trong mảng qua mỗi lần duyệt qua shifts
    # Sau đó, ta cộng dồn từng phần tử của mảng prefix_shift để được mảng shift thực sự(vì những phần tử sau sẽ có độ thay đổi là = độ thay đổi phần tử trước + độ thay đổi phần tử đó)

    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pre_shift = [0] * (len(s) + 1)
        for start, end, direct in shifts:
            if direct == 0:
                pre_shift[start] += -1
                pre_shift[end + 1] += 1
            else:
                pre_shift[start] += 1
                pre_shift[end + 1] += -1

        shift = [pre_shift[0]]
        for i in range(1, len(pre_shift) - 1):
            shift.append(shift[-1] + pre_shift[i])
        res = ''
        for i in range(len(s)):
            res += chr(((ord(s[i]) + shift[i]) - 97) % 26 + 97)
        return res
