class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        
        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[i] >= nums[j]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        to_reverse = nums[i+1:]
        to_reverse = to_reverse[::-1]
        nums[i+1:] = to_reverse
        print(nums)