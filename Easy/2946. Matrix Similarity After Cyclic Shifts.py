class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n = len(mat[0])
        k = k % n
        for i in mat:
            for j in range(0, n):
                if i[j] != i[(j + k) % n]:
                    return False
        return True
