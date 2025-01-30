class Solution:
    #
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        parent = {}
        child = {}

        def initilize(nums):
            for idx, num in enumerate(nums):
                parent[(num, idx)] = (num, idx)

        def find_root(x):
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find_root(x)
            root_y = find_root(y)
            if root_x != root_y:
                if root_x < root_y:
                    parent[root_y] = root_x
                    child[root_x] = root_y
                else:
                    parent[root_x] = root_y
                    child[root_y] = root_x

        initilize(nums)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= limit:
                    union((nums[i], i), (nums[j], j))

        arr = nums[:]
        arr.sort()

        res = []
        for idx, num in enumerate(nums):
            root = find_root((num, idx))
            res.append(root)
            parent[child[root]] = child[root]
        return res
