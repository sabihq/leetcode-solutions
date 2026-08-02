class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9];
        boolean[][] columns = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                char current = board[row][col];

                if (current == '.') {
                    continue;
                }

                int number = current - '1';
                int boxIndex = (row / 3) * 3 + (col / 3);

                if (rows[row][number] ||
                    columns[col][number] ||
                    boxes[boxIndex][number]) {
                    return false;
                }

                rows[row][number] = true;
                columns[col][number] = true;
                boxes[boxIndex][number] = true;
            }
        }

        return true;
    }
}