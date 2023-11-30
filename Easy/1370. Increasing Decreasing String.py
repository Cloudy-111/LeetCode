class Solution:
    def sortString(self, s: str) -> str:
        dic = dict()

        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        sort_dic = dict(sorted(dic.items(), key=lambda item: item[0]))
        res = ''
        cnt = 1
        while len(res) != len(s):
            tmp = ''
            for i in sort_dic:
                if sort_dic[i] != 0:
                    tmp += i
                    sort_dic[i] -= 1
            if cnt % 2 != 0:
                res += tmp[::-1]
            else:
                res += tmp
            cnt += 1
        return res
