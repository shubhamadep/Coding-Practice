class Solution(object):
    def maxArea(self, h):

        left = 0
        right = len(h)-1
        _max = 0

        while left < right:
            container_volume = min(h[left], h[right]) * (right - left)
            if container_volume > _max:
                _max = container_volume

            if h[left] < h[right]:
                left += 1
            else:
                right -= 1

        return _max
        
