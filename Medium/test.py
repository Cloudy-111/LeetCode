a = [1, 2, 3, 4]
dic = {}
m = 0
for i in a:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1
    m = max(dic[i], m)
print(len(dic))
res = []
while m > 0:
    a = []
    for i in dic:
        if dic[i] > 0:
            a.append(i)
            dic[i] -= 1
    res.append(a)
    m -= 1
print(res)
