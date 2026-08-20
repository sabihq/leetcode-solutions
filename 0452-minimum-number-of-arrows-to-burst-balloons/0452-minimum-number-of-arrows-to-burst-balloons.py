class Solution(object):
    def findMinArrowShots(self, points):
        # Sort balloons by their ending position
        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_position = points[0][1]

        for start, end in points[1:]:
            # If this balloon starts after the current arrow,
            # we need another arrow
            if start > arrow_position:
                arrows += 1
                arrow_position = end

        return arrows