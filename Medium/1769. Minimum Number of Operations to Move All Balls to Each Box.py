class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        dis = []
        for i in range(len(boxes)):
            if boxes[i] == '1':
                dis.append(i)
        res = [sum(dis)]
        for i in range(1, len(boxes)):
            tmp = 0
            for j in dis:
                j = abs(j - i)
                tmp += j
            res.append(tmp)
        return res
