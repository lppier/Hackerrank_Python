
def longest_sub(A):
    nds = [1] * len(A)
    for i in range(len(A)):
        maxlenlist = []
        for j in range(0, i):
            if A[j] < A[i]:
                maxlenlist.append(1 + nds[j])
        
        nds[i] = max(maxlenlist) if len(maxlenlist) > 0 else 1
    return max(nds)

longest_sub([0, 8, 4, 12, 2, 10, 6, 14, 1, 9])
