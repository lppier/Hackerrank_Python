# Brute force recursive solution
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        full_list = []
        max_char = n * 2
        
        def helper(A = []):
            if len(A) == max_char:
                if valid(A):
                    full_list.append("".join(A))
            else:
                A.append('(')
                helper(A)
                A.pop()
                A.append(')')
                helper(A)
                A.pop()

        def valid(A):
            bal = 0
            for c in A:
                if c == '(': bal += 1
                else: bal -= 1
                if bal < 0: return False
            return bal == 0
        
        helper()
        return full_list

# Recursive solution, only recurse when combinaton is valid 
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        full_list = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * n:
                full_list.append(S)
            
            if left < n:
                backtrack(S + '(', left+1, right)
            
            if right < left:
                backtrack(S + ')', left, right+1)
                
        backtrack()
        return full_list