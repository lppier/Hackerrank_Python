class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        # use hashset for O(1) look ups, assume no duplicates
        num_set = set(nums)

        for num in num_set:
            current_num = num
            current_streak = 1

            # check if this number is part of another sequence
            if current_num - 1 in num_set:  # eg 4 will be part of 3,4 so ignore starting from 4
                continue

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

        return longest_streak
