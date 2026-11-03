class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sub_boxes = defaultdict(set)
        row_boxes = defaultdict(set)
        column_boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]==".":
                    continue

                if board[i][j] in row_boxes[i] or board[i][j] in sub_boxes[(i//3,j//3)] or board[i][j] in column_boxes[j]:
                    return False
                
                sub_boxes[(i//3,j//3)].add(board[i][j])
                row_boxes[i].add(board[i][j])
                column_boxes[j].add(board[i][j])
        return True 


                 
        