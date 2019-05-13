
import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = sorted(nums1 + nums2)

        if len(combined) % 2 == 0:
            mid_idx = int(len(combined) / 2 - 1)
            return (combined[mid_idx] + combined[mid_idx+1]) / 2
        else:
            mid_idx = math.floor(len(combined)/2)
            return combined[mid_idx]
        