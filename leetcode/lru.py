
# Requirements
# can hold capacity amount of items
# evict keys that are least used when cap is reached

# Everytime an action happens, add 1 to that particular item (age) , age higher, means older
# if i want to evict, evict the one with highest age
# put 1, age1==0, put2, age2==0, get(1) , reset 1, but inc 2
# when 3 comes in, cap reached, looks for highest ,which is 2

import math

class LRUCache:

    age_dict = {}
    item_dict = {}
    max_cap = 0 
    
    def __init__(self, capacity: int):
        self.max_cap = capacity

    def get(self, key: int) -> int:
        if key in self.item_dict:
            for skey in self.age_dict: # action, inc all ages by 1
                self.age_dict[skey] += 1
            self.age_dict[key] = 0
            return self.item_dict[key]
        else:
            return -1

    def get_key_for_max_val(self,adict):
        max_val = float("-inf")
        max_key = None
        
        for k, v, in adict.items():
            if v > max_val:
                max_key = k
                max_val = v
        return max_key        
        
    def put(self, key: int, value: int) -> None: 
        if len(self.item_dict) == self.max_cap: # need to boot oldest
            oldest_key = self.get_key_for_max_val(self.age_dict)
            self.age_dict.pop(oldest_key) 
            self.item_dict.pop(oldest_key)
                
        if key not in self.item_dict:
            self.item_dict[key] = value
            self.age_dict[key] = 0

