# buildings [startx, endx, height]

class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(buildings)
        if n==0:
            return []
        
        if n==1:
            startx, endx, height = buildings[0]
            return [[startx, height], [endx, 0]]
        
        left_skyline = self.getSkyline(buildings[:n//2])
        right_skyline = self.getSkyline(buildings[n//2:])
        
        return self.merge_skylines(left_skyline, right_skyline)
    
    def merge_skylines(self, left, right):
        
        # left / right skyline format is [[x1, y], [x2, 0]]
        
        def update_output(x, y):
            """
            Update the final output with the new element.
            """
            # if skyline change is not vertical - 
            # add the new point
            if not output or output[-1][0] != x:
                output.append([x, y])
            # if skyline change is vertical - 
            # update the last point
            else:
                output[-1][1] = y # x is the same, just change the last output
                
        def append_skyline(p, lst, n, y, curr_y):
            """
            Append the rest of the skyline elements with indice (p, n)
            to the final output.
            """
            while p < n: 
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y
                
        n_l, n_r = len(left), len(right)
        p_l = 0 
        p_r = 0 # index pter for left and right buildings respectively 
        curr_y = left_y = right_y = 0
        output = []
        
        while p_l < n_l and p_r < n_r:
            point_l, point_r = left[p_l], right[p_r]
            # pick smallest x
            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1
            else:
                x, right_y = point_r
                p_r += 1
            
            max_y = max(left_y, right_y)
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y
        
        append_skyline(p_l, left, n_l, left_y, curr_y)
        append_skyline(p_r, right, n_r, right_y, curr_y)
        
        return output
