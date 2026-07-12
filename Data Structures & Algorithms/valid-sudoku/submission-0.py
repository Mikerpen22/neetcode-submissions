class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # target (time, space complexity) = O(n^2), O(n^2)
        from collections import defaultdict
        rowSet = defaultdict(set)
        colSet = defaultdict(set)
        squareSet = defaultdict(set)


        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in rowSet[i]:
                    rowSet[i].add(board[i][j])
                else:
                    return False
                if board[i][j] not in colSet[j]:
                    colSet[j].add(board[i][j])
                else:
                    return False

                sq_i, sq_j = i // 3, j // 3 
                if board[i][j] not in squareSet[(sq_i, sq_j)]:
                    squareSet[(sq_i, sq_j)].add(board[i][j])
                else:
                    return False
        return True
                



        

