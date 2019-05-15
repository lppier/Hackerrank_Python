 
# Caching solution (Dynamic Programming)
class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_water_held = 0
        max_cache_left = {}
        max_cache_right = {}
        
        # get all the maxes for each index from the left
        if len(height) > 0:
            max_left = height[0] 
            for l in range(0, len(height)):
                max_left = max(max_left, height[l])
                max_cache_left[l] = max_left

            # get all the maxes for each index from the right
            max_right = height[len(height)-1]
            for r in reversed(range(0, len(height))):
                max_right = max(max_right, height[r])
                max_cache_right[r] = max_right

            for i in range(len(height)):
                own_depth = height[i]

                # get the minimum of both 
                this_element_water = min(max_cache_left[i], max_cache_right[i]) - own_depth
                if this_element_water < 0:
                    this_element_water = 0
                total_water_held += this_element_water

            return total_water_held
        
        return 0
        
# Brute force solution - does not pass timing
class Solution:
    def trap(self, height: List[int]) -> int:
        
        total_water_held = 0
        
        for i in range(len(height)):
            own_depth = height[i]
            
            # get the max on the left
            max_left = max_right = -1 
            for l in range(0, i):
                max_left = max(max_left, height[l])
            
            # get the max on the right
            for r in range(i+1, len(height)):
                max_right = max(max_right, height[r])
            
            # get the minimum of both 
            water_held_for_this_element = min(max_left, max_right) - own_depth
            if water_held_for_this_element < 0:
                water_held_for_this_element = 0
            total_water_held += water_held_for_this_element
        
        return total_water_held