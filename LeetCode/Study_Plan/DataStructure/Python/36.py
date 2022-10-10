from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row_col_check(board):
            for i in range(9):
                row_cnt_dict = {}
                col_cnt_dict = {}
                for j in range(9):
                    if board[i][j] != ".":
                        if board[i][j] in row_cnt_dict:
                            return False
                        else:
                            row_cnt_dict[board[i][j]] = 1
                    if board[j][i] != ".":
                        if board[j][i] in col_cnt_dict:
                            return False
                        else:
                            col_cnt_dict[board[j][i]] = 1
            return True
        row_status = row_col_check(board)
        print(row_status)

        for i in range(0,9,3):
            for j in range(0,9,3):
                block_cnt_dict = {}
                for k in range(3):
                    for l in range(3):
                        if board[i + k][j + l] != ".":
                            if board[i + k][j + l] in block_cnt_dict:
                                return False
                            else:
                                block_cnt_dict[board[i + k][j + l]] = 1
                        #print(str(i + k) + ',' + str(j + l), end = " ")
                    #print()
                #print('--------------')
        return row_status

if __name__=="__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
             ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."],
             ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
             ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."],
             [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solObj = Solution()
    solObj.isValidSudoku(board)