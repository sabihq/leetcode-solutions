class Solution:
    def summaryRanges(self, nums):
        ranges = []

        if not nums:
            return ranges

        start = nums[0]

        for i in range(1, len(nums)):
            # A gap means the current range has ended
            if nums[i] != nums[i - 1] + 1:
                end = nums[i - 1]

                if start == end:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(end))

                start = nums[i]

        # Add the final range
        end = nums[-1]

        if start == end:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(end))

        return ranges