from collections import defaultdict


a = 'iiiiii'
b = 'zzzyyy'
print(a.count('ie'))
dic = defaultdict(int)
for i in a:
    dic[i] += 1
print(dic)
print(dic['b'])
print(set(a + b))
