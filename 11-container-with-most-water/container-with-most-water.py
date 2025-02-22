class Solution:
    def maxArea(self, height: List[int]) -> int:
            if len(height) < 10**4  or len(height) >2:
                # max_area=0
                # for i in range(len(height)):
                #     for j in range(i,len(height)):
                #         max_area= max(max_area, (j-i) * min(height[i],height[j]) )
                # return max_area
                i=0
                j=len(height) -1
                max_area=0
                while i<j:
                    max_area= max(max_area, (j-i) * min(height[i],height[j]))
                    if height[i] < height [j]:
                        i+=1
                    else:
                        j-=1
                return max_area