

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def helper(s, wordDict, start):

            if start == len(s):
                return True

            for end in range(start+1, len(s)+1):
                substr = s[start:end]
                found_in_wordDict = False

                if substr in wordDict:
                    found_in_wordDict = True

                if found_in_wordDict and helper(s, wordDict, end):
                    return True

            return False

        return helper(s, wordDict, 0)
