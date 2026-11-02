class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        m = len(board[0])
        n = len(board)
        seen = set()
        def dfs(i,j,length):
            if board[i][j] != word[length]:
                return False

            if length == len(word)-1:
                return True
            for r,c in directions:
                new_i =r+i
                new_j =c+j
                if new_i >= 0 and new_i < n  and new_j >= 0 and new_j < m and (new_i, new_j) not in seen:
                    seen.add((new_i,new_j))
                    if dfs(new_i,new_j,length + 1):
                        return True
                    seen.remove((new_i,new_j))
            return False


        for i in range(n):
            for j in range(m):
                seen = set()
                seen.add((i,j))
                if dfs(i,j, 0):
                    return True
        return False

