
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s)==0:
            return True
        
        stack.append(s[0])
        for i in range(1, len(s)):
            if s[i]==')':
                if len(stack)>0 and stack.pop() =='(':
                    continue
                else:
                    return False
            elif s[i]=='}':
                if len(stack)>0 and stack.pop() == '{':
                    continue
                else:
                    return False
            elif s[i]==']':
                if len(stack)>0 and stack.pop() == '[':
                    continue
                else:
                    return False
            else:
                stack.append(s[i])
            
            
        if len(stack)==0:
            return True
        else:
            return False