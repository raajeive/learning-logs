class Solution:
    def maxArea(self, height) -> int:
        if len(height) <= 1:
            return 0
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            max_water = max(max_water, (right - left) * min(height[left], height[right]))
            if height[right] > height[left]:
                left = left + 1
            else:
                right = right - 1
        
        return max_water
