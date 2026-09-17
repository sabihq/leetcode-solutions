class Solution(object):
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0

        while i < len(words):
            # Find how many words fit on the current line
            j = i
            letters = 0

            while (j < len(words) and
                   letters + len(words[j]) + (j - i) <= maxWidth):
                letters += len(words[j])
                j += 1

            number_of_words = j - i
            gaps = number_of_words - 1

            # Last line or a line containing only one word
            if j == len(words) or gaps == 0:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                total_spaces = maxWidth - letters
                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for k in range(i, j - 1):
                    line += words[k]

                    spaces = spaces_per_gap

                    # Left gaps receive the remaining extra spaces
                    if k - i < extra_spaces:
                        spaces += 1

                    line += " " * spaces

                line += words[j - 1]

            result.append(line)
            i = j

        return result