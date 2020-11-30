import java.util.*;


public class Main {
    static int N;
    static int M;
    static char arr[][];
    static int minValue;

    public static void main(String arg[]) {
        Scanner sc = new Scanner(System.in);
        int answer1;
        int answer2;
        int res;
        char color;
        N = sc.nextInt();
        M = sc.nextInt();
        sc.nextLine();
        arr = new char[N][M];
        minValue = 987654321;
        for (int row = 0; row < N; row++) {
            String temp = sc.nextLine();
            for (int col = 0; col < M; col++) {
                arr[row][col] = temp.charAt(col);
            }
        }

        for (int row = 0; row < N - 8 + 1; row++) {
            for (int col = 0; col < M - 8 + 1; col++){
                color = arr[row][col];
                answer1 = 0;
                answer2 = 0;
                for (int i = row; i < row + 8; i++) {
                    for (int j = col; j < col + 8; j++) {
                        if ((i + j - row - col) % 2 == 1) {
                            if (color == arr[i][j]) {
                                answer1++;
                            } else {
                                answer2++;
                            }
                        } else {
                            if (color != arr[i][j]) {
                                answer1++;
                            }
                            else {
                                answer2++;
                            }
                        }
                    }
                }
                res = Math.min(answer1, answer2);
                if (res < minValue) {
                    minValue = res;
                }
            }
        }
        System.out.print(minValue);
    }
}