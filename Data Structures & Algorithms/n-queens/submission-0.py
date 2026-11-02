class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()  # i + j
        diag2 = set()  # i - j  
        queen_placed = 0 
        result = []
        def backtrack(r):
            nonlocal queen_placed
            
            if queen_placed == n:
                ans = ["".join(line) for line in board]
                result.append(ans[::])
                return 
        
            for c in range(n):
                if c not in cols and r+c not in diag1 and r-c not in diag2:
                    queen_placed+=1 
                    diag1.add(r+c)
                    diag2.add(r-c)
                    cols.add(c)
                    board[r][c] = "Q"
                    backtrack(r+1)
                    board[r][c] = "."
                    queen_placed-=1 
                    diag1.remove(r+c)
                    diag2.remove(r-c)
                    cols.remove(c)


                    

        backtrack(0)
        return result
        
                    


                    
        