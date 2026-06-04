class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board)):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row_set[r]) or (board[r][c] in col_set[c]) or (board[r][c] in square[r // 3, c // 3]):
                    return False
                
                row_set[r].add(board[r][c])
                col_set[c].add(board[r][c])
                square[r // 3, c // 3].add(board[r][c])
        
        return True
            