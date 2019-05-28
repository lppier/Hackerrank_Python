class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1] # defines direction for row, we can just use add to move
        dc = [1, 0, -1, 0] # defines direction for col, we can just use add to move
        r = c = 0 # curr direction
        di = 0 # facing, used as idx for dr, dc
        
        for _ in range(R*C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di] # find next move
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                # change direction
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]

        return ans