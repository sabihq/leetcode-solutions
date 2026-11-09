class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []

        for char in reversed(expression):
            if stack and stack[-1] == '?':
                stack.pop()
                true_val = stack.pop()
                stack.pop()
                false_val = stack.pop()

                if char == 'T':
                    stack.append(true_val)
                else:
                    stack.append(false_val)
            else:
                stack.append(char)

        return stack[-1]
