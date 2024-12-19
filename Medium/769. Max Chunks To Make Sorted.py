# Ý tưởng là sử dụng stack để lưu lại giá trị lớn nhất tại thời điểm đó,
# nếu giá trị tiếp theo nhỏ hơn giá trị lơn nhất đó thì pop dần ra khỏi stack và thêm lại giá trị tiếp thoe vào stack
# như vậy trong stack giờ đây chỉ lưu lại những giá trị tăng dần và kết quả sẽ là độ dài của stack đóđó

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        s = []
        for i in range(len(arr)):
            if len(s) == 0 or arr[i] > s[-1]:
                s.append(i)
            else:
                max_element = s[-1]
                while len(s) and s[-1] > arr[[i]]:
                    s.pop()
                s.append(max_element)
        return len(s)
