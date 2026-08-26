class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, opened, closed):
            # A complete combination contains n opening and n closing parentheses
            if len(current) == 2 * n:
                result.append(current)
                return

            # Add "(" if we still have opening parentheses available
            if opened < n:
                backtrack(current + "(", opened + 1, closed)

            # Add ")" only when it can match an existing "("
            if closed < opened:
                backtrack(current + ")", opened, closed + 1)

        backtrack("", 0, 0)
        return result