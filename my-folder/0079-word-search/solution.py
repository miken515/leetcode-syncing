class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def backtrack(row, col, suffix, board):
            if len(suffix) == 0:
                return True
            
            if (
                row < 0 or
                row == ROWS or
                col < 0 or
                col == COLS
                or board[row][col] != suffix[0]
            ):
                return False
            
            ret = False
            board[row][col] = '#'
            
            for nr, nc in directions:
                ret = backtrack(row + nr, col + nc, suffix[1:], board)
                if ret:
                    break

            board[row][col] = suffix[0]

            return ret


        for r in range(ROWS):
            for c in range(COLS):
                if backtrack(r, c, word, board):
                    return True
        return False

        
