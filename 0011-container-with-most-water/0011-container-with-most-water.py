class Solution(object):
    def maxArea(self, height):
        # max=0
        # for i in range(0,len(height)):
        #     for j in range(0,len(height)):
        #         area=min(height[i],height[j])*(j-i)
        #         if area>max:
        #             max=area
        # return max
        # left, right = 0, len(height) - 1
        # max_area = 0
        # while left < right:
        #     width = right - left
        #     area = min(height[left], height[right]) * width
        #     max_area = max(max_area, area)
            
        #     if height[left] < height[right]:
        #         left += 1
        #     else:
        #         right -= 1
        # return max_area

        i=0
        j=len(height)-1
        max_area=0
        while i<j:
            width=j-i
            heights=min(height[i],height[j])
            area=width*heights
            if area>max_area:
                max_area=area
            if height[j]>height[i]:
                i=i+1
            else:
                j=j-1
        return max_area
            

