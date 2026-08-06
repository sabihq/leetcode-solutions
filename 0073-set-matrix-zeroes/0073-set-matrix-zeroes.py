class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if the first row needs to become zero
        for col in range(cols):
            if matrix[0][col] == 0:
                first_row_zero = True

        # Check if the first column needs to become zero
        for row in range(rows):
            if matrix[row][0] == 0:
                first_col_zero = True

        # Mark rows and columns using the first row and column
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        # Set the marked rows and columns to zero
        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        # Zero out the first row
        if first_row_zero:
            for col in range(cols):
                matrix[0][col] = 0

        # Zero out the first column
        if first_col_zero:
            for row in range(rows):
                matrix[row][0] = 0