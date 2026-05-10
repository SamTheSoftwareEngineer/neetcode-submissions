class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set) # key: r // 3, c // 3

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                # If the current number is already inside the current row,
                # we found a duplicate 
                if (board[r][c] in row[r] 
                    or board[r][c] in col[c]
                    or board[r][c] in square[(r//3, c//3)]):
                        return False

                col[c].add(board[r][c])
                row[r].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])

        return True
                    
