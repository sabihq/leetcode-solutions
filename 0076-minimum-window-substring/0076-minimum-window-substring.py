class Solution(object):
    def minWindow(self, s, t):
        if len(t) > len(s):
            return ""

        need = {}
        for char in t:
            need[char] = need.get(char, 0) + 1

        window = {}
        required = len(need)
        formed = 0
        left = 0

        min_length = float("inf")
        min_start = 0

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    min_start = left

                left_char = s[left]
                window[left_char] -= 1

                if left_char in need and window[left_char] < need[left_char]:
                    formed -= 1

                left += 1

        if min_length == float("inf"):
            return ""

        return s[min_start:min_start + min_length]