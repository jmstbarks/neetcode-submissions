class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0
        while left <= right:
            if heights[left] < heights[right]:
                currentArea = (right - left) * heights[left]
                left +=1
            else:
                currentArea = (right - left) * heights[right]
                right -= 1
            res = max(res, currentArea)
        return res