# iterate through each element
#   go through each element to the right of it to see total count of smaller elements
# O(n^2)


class Solution:

    #     # brute force (not accepted)
    #     def countSmaller(self, nums: List[int]) -> List[int]:
    #         counts = []

    #         for i in range(len(nums)):
    #             count = 0
    #             val = nums[i]
    #             for j in range(i+1, len(nums)):
    #                 if nums[j] < val:
    #                     count += 1
    #             counts.append(count)

    #         return counts

    # mergesort soln O(nlogn)
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                m, n = len(left), len(right)
                i = j = k = 0

                # this is a standard mergesort algorithm
                # introduction of smaller[] to track, number of smaller than current element
                # looking at i, which is j
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[k] = left[i]
                        # addition, by original val idx
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[k] = right[j]
                        j += 1
                    k += 1

                while i < m:
                    enum[k] = left[i]
                    k += 1
                    i += 1

                while j < n:
                    enum[k] = right[j]
                    k += 1
                    j += 1

            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller
