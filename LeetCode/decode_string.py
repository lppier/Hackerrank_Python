class Solution:

    def strMultiplier(self, astr, n):
        returnstr = ""
        for i in range(n):
            returnstr += astr
        return returnstr

    def decodeString(self, s: str) -> str:
        stk = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                digit_str = s[i]
                k = i+1
                while k < len(s) and s[k].isdigit():
                    digit_str = digit_str + s[k]
                    k += 1
                stk.append(int(digit_str))
                i = k
                continue
            elif s[i] == '[':
                stk.append(s[i])
            elif s[i] == ']':
                temp_stk = []
                while stk and not type(stk[-1]) == int:
                    temp = stk.pop()
                    if temp != '[' and temp != ']':
                        temp_stk.insert(0, temp)

                transform_str = self.strMultiplier("".join(temp_stk), stk[-1])
                stk.pop()
                stk.append(transform_str)
            else:  # a - z
                stk.append(s[i])
            i += 1

        return "".join(stk)
