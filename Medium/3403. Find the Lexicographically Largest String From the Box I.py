class Solution:
    # Đề bài yêu cầu tìm chuỗi con lớn nhất có thể tạo từ chuỗi ban đầu sau khi chia thành numFriends chuỗi
    # Để tìm chuỗi con lớn nhất, ta cần tìm ký tự lớn nhất trong chuỗi ban đầu, lưu các vị trí của ký tự đó trong mảng split
    # Để ý một chút, chuỗi con lớn nhất sẽ là chuỗi con bắt đầu bằng ký tự lớn nhất đó và có độ dài là len(word) - numFriends + 1 --> đọc kĩ đề bài sẽ thấy
    # Vì vậy, ta chỉ cần duyệt qua mảng split, lấy chuỗi con từ vị trí split[i] đến split[i] + len(word) - numFriends + 1, so sánh các chuỗi và đưa ra kết quả
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        char = max(word)
        split = []
        for i in range(len(word)):
            if word[i] == char:
                split.append(i)

        max_len = len(word) - numFriends + 1
        max_string = ''
        for i in range(len(split)):
            max_string = max(max_string, word[split[i]: split[i] + max_len])
        return max_string


class Solution:
    # Có thể lược bót mảng split, chỉ cần duyệt qua mảng ban đầu, chỗ nào là kí tự lớn nhất thì so sánh chuỗi con được tạo ra từ đó
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        char = max(word)

        max_len = len(word) - numFriends + 1
        max_string = ''
        for i in range(len(word)):
            if word[i] == char:
                max_string = max(max_string, word[i: i + max_len])
        return max_string
