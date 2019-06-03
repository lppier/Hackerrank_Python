# Question: We are interested in getting 7 digit phone number by watching a chess piece (rook) traverse a board with numbers on each board position.

# Given a 3 by 3 board that looks like this.

# 1 2 3
# 4 5 6
# 7 8 9

# And assuming that a rook starts on position 4, write a function which provides all of the combinations of 7 digit numbers which start with 4.

# For example:

# 456-3214 would be generated when the rook moves
# { right one, right one, up one, left one, left one, down one }

# 464-6464 would be generated when the rook moves
# {right two, left two, right two, left two, right two, left two }

def chess_dialer():
    
    map_ = {
        1 : [2, 3, 4, 7],
        2 : [1, 3, 5, 8],
        3 : [1, 2, 6, 9],
        4 : [1, 7, 5, 6],
        5 : [2, 8, 4, 6],
        6 : [3, 9, 4, 5],
        7 : [1, 4, 8, 9],
        8 : [2, 5, 7, 9],
        9 : [3, 6, 7, 8]
    }
    
    def backtrack(res, curr):
        if len(curr) == 7:
            res.append(curr[:])
            return
        
        for ele in map_[curr[-1]]:
            curr.append(ele)
            backtrack(res, curr)
            curr.pop()
    
    res, curr = [], [4]
    backtrack(res, curr)
    return res