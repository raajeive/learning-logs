class Solution:
    def maxArea(self, height):
        first = 0
        last = len(height) - 1
        area = 0
        while first < last:
            area = max(area, min(height[first], height[last]) * (last - first))
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
        return area
