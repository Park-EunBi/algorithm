class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        # sol_1 - 첫 행의 맨 뒤에서 탐색
        if not matrix:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while row <= len(matrix) -1 and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False
        '''

        # sol_2
        return any(target in row for row in matrix)