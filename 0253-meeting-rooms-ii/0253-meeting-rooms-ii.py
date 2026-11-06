class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        rooms = 0
        end_ptr = 0

        for start in starts:
            if start < ends[end_ptr]:
                rooms += 1
            else:
                end_ptr += 1

        return rooms