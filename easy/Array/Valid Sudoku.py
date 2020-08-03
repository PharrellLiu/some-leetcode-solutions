from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dicForRow = {}
        dicForCol = {0: {}, 1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}, 7: {}, 8: {}}
        dicForSq = {0: {}, 1: {}, 2: {}}
        i = 0
        while i < 9:
            j = 0
            while j < 9:
                if board[i][j] != ".":
                    if board[i][j] in dicForRow:
                        return False
                    else:
                        dicForRow[board[i][j]] = 1
                    if board[i][j] in dicForCol[j]:
                        return False
                    else:
                        dicForCol[j][board[i][j]] = 1
                    if board[i][j] in dicForSq[j // 3]:
                        return False
                    else:
                        dicForSq[j // 3][board[i][j]] = 1
                j += 1
            dicForRow.clear()
            i += 1
            if i == 3 or i == 6:
                dicForSq.clear()
                dicForSq = {0: {}, 1: {}, 2: {}}
        return True
