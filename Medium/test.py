a = [3, 4, 5]
res = a[0]
for i in range(1, len(a)):
    res = res ^ a[i]
print(res)
