def minArraySum(nums, k):
    n = len(nums)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + nums[i]

    print(prefix)
    res = prefix[n]
    last = -1
    for i in range(1, n + 1):
        if prefix[i] % k == 0:
            last = prefix[i]
            prefix[i] = 0

    print(prefix)
    for i in range(n, -1, -1):
        if prefix[i] == 0:
            if last != -1:
                res -= last
            break
    return res


nums = [36, 78, 29, 83, 81, 87, 45, 66, 63, 28]
k = 93

print(minArraySum(nums, k))
