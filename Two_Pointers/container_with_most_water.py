class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # We know that this is a 2 pointer problem. because the pointers will move from opposite sides, we MUST initiate both 
        L = 0 
        R = len(height) - 1 

        # Think about what we need to return. Therefore we need an area variable
        area = 0 


        # Its typical when we see a 2 pointer in opposite problem to set up a while loop while L doesnt overrun r 
        while L < R:
            # we want to do a few things 
            # 1) calculate the width and area
            # 2) update the area ONLY if its the new max 
            width = R - L
            minheight = min(height[R], height[L])
            newArea = width * minheight
            area = max(area, newArea) 

            if height[L] > height[R]:
                R -= 1 
            else: # else if we have the R pointer is higher OR if they are same then can move up L
            # but again if they are the same we can move either one
                L += 1

        
        return area
