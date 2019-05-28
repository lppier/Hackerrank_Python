# "2, 3, 4" 
# time complexity : 3^ n 
# 23 23 'a d', have combinations of all the 2, 3s two two numbers

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dlist = list(digits)
        print(dlist)
        ans = []
        lookup = {}
        lookup[2] = 'abc'
        lookup[3] = 'def'
        lookup[4] = 'ghi'
        lookup[5] = 'jkl'
        lookup[6] = 'mno'
        lookup[7] = 'pqrs'
        lookup[8] = 'tuv'
        lookup[9] = 'wxyz'
        
        def helper(d_list_num, str_so_far):
            if d_list_num == []:
                return str_so_far 
            
            char_str = lookup[int(d_list_num[0])]
            for char in char_str: 
                astr = helper(d_list_num[1:], str_so_far + char)
                if astr:
                    ans.append(astr)            
                
        helper(dlist, "")
        return ans