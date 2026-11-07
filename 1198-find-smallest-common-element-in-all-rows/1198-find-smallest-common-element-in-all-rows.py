class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        count = {}

        for row in mat:
            for num in row:
                count[num] = count.get(num, 0) + 1

        for num in mat[0]:
            if count[num] == len(mat):
                return num

        return -1