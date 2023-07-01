class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        maxArea = 0 
        while l <= r:
            area = min(height[l], height[r]) * (r-l) # the height will be the minimum of these 2 heights 
            maxArea = max(area, maxArea)
            if height[l] > height[r]:
                r -= 1 
            # elif height[r] > height[l]: 
            #     l += 1
            # else: 
            #     # if they are equal we can move either pointer
            #     l += 1
            # we can really just put bother together 
            else: 
                l += 1

        return maxArea