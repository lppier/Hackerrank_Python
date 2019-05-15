class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        new_list = []
        i = 0
        while i < len(intervals):
            print(f'i = {i}')
            temp_interval = intervals[i]
            print(f'temp {temp_interval}')
            j = i+1
            while j < len(intervals) and temp_interval[1] >= intervals[j][0]:
                if intervals[j][1] >= temp_interval[1]:
                    temp_interval = [temp_interval[0], intervals[j][1]]
                # otherwise, no chance to temp_interval
                print(f'temp {temp_interval}')
                j += 1
            new_list.append(temp_interval)
            i = j
            print(f'j = {j}')
        return new_list
