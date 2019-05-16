# priority queue using min-heap soln
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals)==0:
            return 0
        
        intervals = sorted(intervals)
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1]) # push the end time of 1st item
        
        for i in intervals[1:]:
            # check if smallest end time in min-heap is lower than start time of interval coming in
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms) # simulate 'reusing' the room, pop out, add new end time next line
            heapq.heappush(free_rooms, i[1]) 
        
        return len(free_rooms)



# Chronological ordering approach
class Solution(object):
    def minMeetingRooms(self, intervals):
 
        # If there are no meetings, we don't need any rooms.
        if not intervals:
            return 0

        used_rooms = 0

        # Separate out the start and the end timings and sort them individually.
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted(i[1] for i in intervals)
        L = len(intervals)

        # The two pointers in the algorithm: e_ptr and s_ptr.
        end_pointer = 0
        start_pointer = 0

        # Until all the meetings have been processed
        while start_pointer < L:
            # If there is a meeting that has ended by the time the meeting at `start_pointer` starts
            if start_timings[start_pointer] >= end_timings[end_pointer]:
                # Free up a room and increment the end_pointer.
                used_rooms -= 1
                end_pointer += 1

            # We do this irrespective of whether a room frees up or not.
            # If a room got free, then this used_rooms += 1 wouldn't have any effect. used_rooms would
            # remain the same in that case. If no room was free, then this would increase used_rooms
            used_rooms += 1    
            start_pointer += 1   

        return used_rooms