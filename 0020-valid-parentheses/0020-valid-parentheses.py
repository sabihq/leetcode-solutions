class Solution:
    def isValid(self, s):
        stack = []

        matching = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for bracket in s:
            if bracket in "([{":
                stack.append(bracket)
            else:
                if not stack:
                    return False

                if stack.pop() != matching[bracket]:
                    return False

        return len(stack) == 0