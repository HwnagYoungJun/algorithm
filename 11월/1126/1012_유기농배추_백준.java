import java.util.*;

public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);

        int testCase = sc.nextInt();

        for (int t = 0; t < testCase; t++) {
            int count;
            int M = sc.nextInt();
            int N = sc.nextInt();
            int K = sc.nextInt();
            int[][] arr = new int[N][M];
            boolean[][] visited = new boolean[N][M];

            count = 0;
            for (int i = 0; i < K; i++) {
                int X = sc.nextInt();
                int Y = sc.nextInt();
                arr[Y][X] = 1;
            }

            for (int row = 0; row < N; row++) {
                for (int col = 0; col < M; col++) {
                    if (arr[row][col] == 0) {
                        continue;
                    }
                    if (visited[row][col]) {
                        continue;
                    }
                    bfs(row, col, arr, visited);
                    count++;
                }
            }
            System.out.println(count);
        }
    }
    public static void bfs(int row, int col, int[][] arr, boolean[][] visited) {
        Queue<int[]> queue = new LinkedList<>();
        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};
        arr[row][col] = 1;
        queue.offer(new int[] {row, col});
        while (!queue.isEmpty()) {
            int[] temp = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nr = temp[0] + dr[i];
                int nc = temp[1] + dc[i];

                if (nr < 0 || nr >= arr.length || nc < 0 || nc >= arr[0].length) {
                    continue;
                }
                if (visited[nr][nc] || arr[nr][nc] == 0) {
                    continue;
                }
                visited[nr][nc] = true;
                queue.offer(new int[] {nr, nc});
            }
        }
    }
}