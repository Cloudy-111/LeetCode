def xorAfterQueries(nums, queries):
    n = len(nums)
    q = len(queries)
    for i in queries:
        l, r, k, v = i[0], i[1], i[2], i[3]
        for j in range(l, r + 1, k):
            nums[j] = (nums[j] * v) % (10**9 + 7)

    res = nums[0]
    for i in range(1, n):
        res = res ^ nums[i]

    return res


nums = [2, 3, 1, 5, 4]
queries = [[1, 4, 2, 3], [0, 2, 1, 2]]

print(xorAfterQueries(nums, queries))
