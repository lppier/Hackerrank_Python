
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

        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

            # check that we use the smaller array to do binary search
            if len(nums1) > len(nums2):
                return self.findMedianSortedArrays(nums2, nums1)
            
            A, B = nums1, nums2
            lenA = len(A)
            lenB = len(B)
            start = 0
            end = len(A)
            i, j = 0, 0
            print(lenA, lenB)

            while (start <= end):
                i = math.floor((start + end) / 2)
                j = math.floor((lenA + lenB + 1) / 2) - i
                print(f'i = {i}, j={j}')
                maxLeftA = -math.inf if i == 0 else A[i-1]
                maxLeftB = -math.inf if j == 0 else B[j-1]
                minRightA = math.inf if i == lenA else A[i]
                minRightB = math.inf if j == lenB else B[j]
                print(maxLeftA, maxLeftB, minRightA, minRightB)

                if maxLeftA <= minRightB and maxLeftB <= minRightA:
                    if (lenA + lenB) % 2 == 0:
                        return (max(maxLeftA, maxLeftB) + min(minRightB, minRightA)) / 2.0
                    else:
                        return max(maxLeftA, maxLeftB)

                if maxLeftA > minRightB:
                        end = i - 1
                elif maxLeftB > minRightA:
                        start = i + 1