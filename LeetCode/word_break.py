# Recursion with memoization soln

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        
        def helper(s, wordDict, start):
            if start == len(s):
                return True
            
            if start in memo:
                return memo[start]
            
            for end in range(start+1, len(s)+1):
                substr = s[start:end]
                found_in_wordDict = False

                if substr in wordDict:
                    found_in_wordDict = True

                if found_in_wordDict and helper(s, wordDict, end):
                    memo[start] = True
                    return memo[start]

            memo[start] = False
            return memo[start]

        return helper(s, wordDict, 0)