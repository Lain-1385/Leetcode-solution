#Mine
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        res = min(height[left], height[right]) * (right - left)
        temp = 0

        while(1):
            # move left
            if(height[right] >= height[left]):
                temp = left
                # move temp until h[temp] is taller than h[left]
                while(height[left] >= height[temp]):
                    if(temp >= right):
                        return res
                    temp += 1

                left = temp
                res = max(res, min(height[left], height[right]) * (right - left))

            # move right
            else:
                temp = right

                while(height[right] >= height[temp]):
                    if(temp <= left):
                        return res
                    temp -= 1

                right = temp
                res = max(res, min(height[left], height[right]) * (right - left))