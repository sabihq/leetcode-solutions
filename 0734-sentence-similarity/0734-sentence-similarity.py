from typing import List

class Solution:
    def areSentencesSimilar(
        self,
        sentence1: List[str],
        sentence2: List[str],
        similarPairs: List[List[str]]
    ) -> bool:
        if len(sentence1) != len(sentence2):
            return False

        pairs = {(a, b) for a, b in similarPairs}

        for a, b in zip(sentence1, sentence2):
            if a == b:
                continue
            if (a, b) not in pairs and (b, a) not in pairs:
                return False

        return True