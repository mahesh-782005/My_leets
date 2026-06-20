class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    val = board[i][j]
                    boxi = (i//3)*3
                    boxj = (j//3)*3
                    for k in range(boxi, boxi+3):
                        for l in range(boxj, boxj+3):
                            if k == i and l== j:
                                continue
                            if board[k][l] == val:
                                return False
                    for k in range(9):
                        if k == i:
                            continue
                        if board[k][j] == val:
                            return False
                    for l in range(9):
                        if l == j:
                            continue
                        if board[i][l] == val:
                            return False
                    
        return True