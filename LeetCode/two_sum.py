class Solution:
    
    # O(n^2) solution
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         for i in range(len(nums)):
#             curr = nums[i]
#             for j in range(i+1, len(nums)):
#                 if curr + nums[j] == target:
#                     return [i, j]
        
#         return None
    
    # O(n) solution, memoization
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache = {}
        for idx, num in enumerate(nums): 
            cache[num] = idx
        for i in range(len(nums)):
            curr = nums[i]
            complement = target - curr
            if complement in cache and cache[complement] != i :
                return [i, cache[complement]]
        return None