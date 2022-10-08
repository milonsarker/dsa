from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def row_check(board):
            for i in range(9):
                cnt_dict = {}
                for j in board[i][:]:
                    if j != ".":
                        if j in cnt_dict:
                            return False
                        else:
                            cnt_dict[j] = 1
            return True
        row_status = row_check(board)

        def col_check(board):
            print('ll')
if __name__=="__main__":
    board =  [["5", "3", ".", ".", "7", ".", ".", ".", "."]
            , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
            , [".", "9", "8", ".", ".", ".", ".", "6", "."]
            , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
            , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
            , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
            , [".", "6", ".", ".", ".", ".", "2", "8", "."]
            , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
            , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    #solObj = Solution()
    #solObj.isValidSudoku(board)
    print(board[1][:])