from collections import Counter
import heapq
import builtins

# Ý tưởng ban đầu: đưa vào priorityqueue 1 cặp là kí tự và tần suất xuất hiện của kí tự đó
# Mỗi lần lấy ra cặp đó, trừ dần số lần xuất hiện, khi số lần bằng repeatLimit hoặc freq = 0 thì thoát vòng lặp
# Sau đó kiểm tra kí tự tiếp theo thêm 1 lần vào và push vào priority, nếu kí trự trước đó còn thì push phần còn lại vào
# Lặp lại cho đến khi queue hết


class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        d = dict(Counter(s))
        res = ""
        lst = [(-builtins.ord(char), freq) for char, freq in d.items()]
        heapq.heapify(lst)
        while lst:
            k = repeatLimit
            ord, freq = heapq.heappop(lst)
            while k > 0:
                res += chr(-ord)
                freq -= 1
                k -= 1
                if freq == 0 or k == 0:
                    break
            if freq > 0 and lst:
                ord1, freq1 = heapq.heappop(lst)
                res += chr(-ord1)
                freq1 -= 1
                if freq1 > 0:
                    heapq.heappush(lst, (ord1, freq1))
                heapq.heappush(lst, (ord, freq))
        return res
