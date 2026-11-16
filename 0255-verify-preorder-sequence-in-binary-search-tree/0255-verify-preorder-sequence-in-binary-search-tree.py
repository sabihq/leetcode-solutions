class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        lower_bound = float('-inf')
        stack_top = -1

        for num in preorder:
            if num < lower_bound:
                return False

            while stack_top >= 0 and num > preorder[stack_top]:
                lower_bound = preorder[stack_top]
                stack_top -= 1

            stack_top += 1
            preorder[stack_top] = num

        return True
