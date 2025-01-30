from typing import List

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        max_area = 0
        n = len(matrix[0])
        heights = [0] * n  # Initialize heights for the histogram

        for row in matrix:
            for i in range(n):
                # Update heights; if the current cell is '1', increment the height
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Calculate the maximal area for the current row's histogram
            max_area = max(max_area, self._largestRectangleArea(heights))
        
        return max_area

    def _largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # Append a sentinel value to handle remaining bars
        stack = []
        max_area = 0
        
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        heights.pop()  # Remove the sentinel value
        return max_area
