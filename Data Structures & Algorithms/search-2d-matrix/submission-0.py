class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l = 0
        r = n*m -1

        while l<= r:
            mid = (l+r) // 2

            row = mid // m 
            column = mid % m 

            if matrix[row][column] == target:
                return True
            elif matrix[row][column] > target:
                r = mid - 1 
            else:
                l = mid + 1
        
           
        return False




        