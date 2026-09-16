from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        words = set(wordList)

        if endWord not in words:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            current_word, sequence_length = queue.popleft()

            if current_word == endWord:
                return sequence_length

            for i in range(len(current_word)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    next_word = (
                        current_word[:i]
                        + letter
                        + current_word[i + 1:]
                    )

                    if next_word in words:
                        words.remove(next_word)
                        queue.append((next_word, sequence_length + 1))

        return 0