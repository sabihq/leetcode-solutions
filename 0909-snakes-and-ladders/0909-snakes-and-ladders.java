import java.util.*;

class Solution {
    public int snakesAndLadders(int[][] board) {
        int n = board.length;
        int target = n * n;

        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[target + 1];

        queue.offer(1);
        visited[1] = true;

        int rolls = 0;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();

            for (int i = 0; i < levelSize; i++) {
                int current = queue.poll();

                if (current == target) {
                    return rolls;
                }

                // Try every possible dice roll
                for (int next = current + 1;
                     next <= Math.min(current + 6, target);
                     next++) {

                    int[] position = getPosition(next, n);
                    int row = position[0];
                    int col = position[1];

                    int destination = next;

                    // Follow one snake or ladder
                    if (board[row][col] != -1) {
                        destination = board[row][col];
                    }

                    if (!visited[destination]) {
                        visited[destination] = true;
                        queue.offer(destination);
                    }
                }
            }

            rolls++;
        }

        return -1;
    }

    private int[] getPosition(int square, int n) {
        int index = square - 1;

        // Number of rows above the bottom row
        int rowFromBottom = index / n;
        int row = n - 1 - rowFromBottom;

        int col = index % n;

        // Every other row goes from right to left
        if (rowFromBottom % 2 == 1) {
            col = n - 1 - col;
        }

        return new int[]{row, col};
    }
}