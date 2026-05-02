class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        vol = 0

        while(left < right):
            curr_height = min(heights[left], heights[right])
            curr_vol = curr_height * ((right + 1) - (left + 1))
            
            if curr_vol > vol:
                vol = curr_vol
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1


        return vol

            