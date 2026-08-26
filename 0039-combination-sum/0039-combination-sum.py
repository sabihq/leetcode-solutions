class Solution(object):
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, current, total):
            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])

                # Use i again because each number can be reused
                backtrack(i, current, total + candidates[i])

                # Undo the choice
                current.pop()

        backtrack(0, [], 0)
        return result