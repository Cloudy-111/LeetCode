class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def initilize(edges):
            for edge in edges:
                for node in edge:
                    parent[node] = node

        def find_root(x):
            if parent[x] != x:
                parent[x] = find_root(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find_root(x)
            root_y = find_root(y)
            if root_x != root_y:
                parent[root_y] = root_x

        initilize(edges)
        for edge in edges:
            root_x = find_root(edge[0])
            root_y = find_root(edge[1])
            if root_x == root_y:
                return edge
            union(edge[0], edge[1])
