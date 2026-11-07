
class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m, k = len(mat1), len(mat1[0])
        n = len(mat2[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(k):
                if mat1[i][j] == 0:
                    continue

                for col in range(n):
                    if mat2[j][col] != 0:
                        result[i][col] += mat1[i][j] * mat2[j][col]

        return result
