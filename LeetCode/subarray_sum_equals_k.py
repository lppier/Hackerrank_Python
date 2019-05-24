class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums:
            return 0

        preSum, ret, size = [0], 0, len(nums)
        count = collections.Counter(preSum)
        if size == 1:
            return 1 if nums[0] == k else 0
        for val in nums:
            s = preSum[-1] + val
            preSum.append(s)
            ret += count.get(s - k, 0)
            count[s] = count.get(s, 0) + 1

        return ret
            