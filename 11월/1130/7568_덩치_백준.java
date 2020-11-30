import java.util.*;


public class Main {
    static int N;
    static int[][] arr;
    static int[] answer;
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        arr = new int[N][2];
        answer = new int[N];

        for (int row = 0; row < N; row++) {
            for (int col = 0; col < 2; col ++){
                arr[row][col] = sc.nextInt();
            }
        }

        for (int i = 0; i < N - 1; i++) {
            for (int j = i + 1; j < N; j++) {
                if (arr[i][0] < arr[j][0] && arr[i][1] < arr[j][1]) {
                    answer[i]++;
                } else  if (arr[i][0] > arr[j][0] && arr[i][1] > arr[j][1]) {
                    answer[j]++;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            System.out.printf("%d ", answer[i] + 1);
        }
    }
}