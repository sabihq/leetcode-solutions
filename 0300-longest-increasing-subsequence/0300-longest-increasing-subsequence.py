class Solution(object):
    def lengthOfLIS(self, nums):
        tails = []

        for num in nums:
            left, right = 0, len(tails)

            # Find the first value in tails that is >= num
            while left < right:
                middle = (left + right) // 2

                if tails[middle] < num:
                    left = middle + 1
                else:
                    right = middle

            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)