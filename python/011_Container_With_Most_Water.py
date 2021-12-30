# class Solution:
#     def maxArea(self, height: List[int]) -> int:
#         # Two points
#         left, right = 0, len(height) - 1
#         result = 0
#         while left < right:
#             result = max(min(height[left], height[right]) * (right - left), result)
#             if height[left] > height[right]:
#                 # remove right
#                 right -= 1
#             else:
#                 # remove left
#                 left += 1
#         return result

# 668 ms	27.6 MB	python3
class Solution:
    def maxArea(self, height):
        L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            if height[L] < height[R]:
                res, L = max(res, height[L] * w), L + 1
            else:
                res, R = max(res, height[R] * w), R - 1
        return res