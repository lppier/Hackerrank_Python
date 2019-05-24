class Solution(object):
    def calculate(self, s):
        nums = []
        sign = 1
        num = 0
        rst = 0
    
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
                continue
            rst += sign*num
            num = 0
        
            if c == "-": sign = -1
            elif c == "+": sign = 1
            elif c == "(":
                nums.append(rst)
                nums.append(sign)
                sign = 1
                rst = 0
            elif c == ")":
                rst *= nums.pop()
                rst += nums.pop()

        return rst + sign * num