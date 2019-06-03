class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        N = len(S)
        match = [-1] * N  # store the idx of all the matching places

        for i in range(len(indexes)):
            ix = indexes[i]
            source_len = len(sources[i])
            if S[ix:ix+source_len] == sources[i]:
                match[ix] = i

        ix = 0
        ans = ""

        while ix < N:
            if match[ix] >= 0:  # if matched, add the replacement string
                ans = ans + targets[match[ix]]
                # inc by ori string len to keep ref. to S
                ix += len(sources[match[ix]])
                print(f"appended {ans}")
            else:  # if no match proceed as usual
                ans += S[ix]
                ix += 1

        return ans
