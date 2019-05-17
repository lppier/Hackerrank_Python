# Recursive solution
class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # if pattern has ended, and we still have characters in s return False
        if not p:
            if s and len(s) > 0:
                return False
            else:
                return True

        match = False
        if s and (s[0] == p[0] or p[0] == '.'):
            match = True

        if len(p) >= 2 and p[1] == '*':
            # encountering '*' in 2nd index:
            #   1st case: we ignore c*, meaning no characters of c can be found in s
            #   2nd case: if we know both matches, we delete 1st c from s, and see if next one in s matches
            return (self.isMatch(s, p[2:])) or (match and self.isMatch(s[1:], p))
        else:
            # straightforward match, delete 1 char from both s and p
            return match and self.isMatch(s[1:], p[1:])

# Recursive solution, improved with dp
class Solution:
    def isMatch(self, s_in: str, p_in: str) -> bool:
        memo = {}
        def dp(s, p):
            if (s, p) not in memo:
                # if pattern has ended, and we still have characters in s return False
                if not p:  
                    if s and len(s) > 0:
                        return False
                    else:
                        return True

                match = False
                if s and (s[0] == p[0] or p[0] == '.'):
                    match = True

                if len(p) >= 2 and p[1] == '*':
                    # encountering '*' in 2nd index:
                    #   1st case: we ignore c*, meaning no characters of c can be found in s
                    #   2nd case: if we know both matches, we delete 1st c from s, and see if next one in s matches
                    ans =  dp(s, p[2:]) or (match and dp(s[1:], p))
                else:
                    # straightforward match, delete 1 char from both s and p
                    ans =  match and dp(s[1:], p[1:])
                
                memo[(s, p)] = ans
            return memo[(s, p)]
            
        return dp(s_in, p_in)