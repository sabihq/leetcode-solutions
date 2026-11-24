class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        n = len(arr)
        diff = (arr[-1] - arr[0]) // n

        for i in range(1, n):
            if arr[i] - arr[i - 1] != diff:
                return arr[i - 1] + diff

        return arr[0]