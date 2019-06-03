class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        occurances = {}

        for char in s:
            if char not in occurances:
                occurances[char] = 1
            else:
                occurances[char] += 1

        pos = 0  # stores position of smallest so far
        char_chosen = ""
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i

            if s[i] in occurances:
                occurances[s[i]] -= 1

            # if we have the smallest so far, and s[i] cannot be eliminated, we have
            # to take the smallest so far
            if occurances[s[i]] == 0:
                char_chosen = s[pos]
                break

        astr = s[pos+1:].replace(char_chosen, "")

        if len(s) == 0:
            return ""
        else:
            return s[pos] + self.removeDuplicateLetters(astr)
