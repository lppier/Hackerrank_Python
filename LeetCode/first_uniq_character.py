class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache = {}
        if len(s) == 0:
            return -1

        def firstUniq(s):

            for idx, char in enumerate(s):
                if char not in cache:
                    cache[char] = idx
                else:
                    cache[char] = -1  # this char does not qualify

            for char in s:
                if cache[char] != -1:
                    return cache[char]
            return -1

        return firstUniq(s)
