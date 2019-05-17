import copy


class Solution:

    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        r_dim = len(board)
        c_dim = len(board[0])
        # immutable copy for referencing, note list.copy() does not work
        board_copy = copy.deepcopy(board)

        for r in range(r_dim):
            for c in range(c_dim):
                live = 0
                curr = board_copy[r][c]

                # check row above
                if r > 0:
                    if c > 0:
                        if board_copy[r-1][c-1] == 1:
                            live += 1
                    if board_copy[r-1][c] == 1:
                        live += 1
                    if c < c_dim-1:
                        if board_copy[r-1][c+1] == 1:
                            live += 1

                # check left and right
                if c > 0:
                    if board_copy[r][c-1] == 1:
                        live += 1
                if c < c_dim-1:
                    if board_copy[r][c+1] == 1:
                        live += 1

                # check bottom row
                if r < r_dim-1:
                    if c > 0:
                        if board_copy[r+1][c-1] == 1:
                            live += 1
                    if board_copy[r+1][c] == 1:
                        live += 1
                    if c < c_dim-1:
                        if board_copy[r+1][c+1] == 1:
                            live += 1
                print(f'cell = [{r}, {c}], live = {live}')
                # conditions
                if curr == 1:
                    if live < 2:
                        board[r][c] = 0
                    elif live == 2 or live == 3:
                        board[r][c] = 1
                    elif live > 3:
                        board[r][c] = 0
                else:
                    if live == 3:
                        board[r][c] = 1
