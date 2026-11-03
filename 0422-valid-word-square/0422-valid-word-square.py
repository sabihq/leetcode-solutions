from typing import List

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i, word in enumerate(words):
            for j, char in enumerate(word):
                if j >= len(words) or i >= len(words[j]):
                    return False
                if char != words[j][i]:
                    return False

        return True