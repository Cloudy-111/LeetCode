def partitionLabels(s: str):
    dic = {}
    s = s + '.'
    for i in range(len(s)):
        if s[i] not in dic:
            dic[s[i]] = [i, i]
        else:
            dic[s[i]][1] = i
    start = dic[s[0]]
    first = start[0]
    last = start[1]
    res = []
    for i in dic:
        tmp = dic[i]
        if tmp[0] > last:
            res.append(last - first + 1)
            first = tmp[0]
            last = tmp[1]
        else:
            last = max(last, tmp[1])
    print(res)


s = 'eccbbbbdec'
partitionLabels(s)
