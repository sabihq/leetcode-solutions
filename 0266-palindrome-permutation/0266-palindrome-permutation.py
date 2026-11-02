class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        odd = set()

        for char in s:
            if char in odd:
                odd.remove(char)
            else:
                odd.add(char)

        return len(odd) <= 1