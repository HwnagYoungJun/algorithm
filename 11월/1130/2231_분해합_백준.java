import java.util.*;


public class Main {
    static int N;
    static int M;
    public static void main(String arg[]){
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        int rest;
        int answer;
        answer = 0;

        for (int j = 0; j < N; j++) {
            int logJ = (int)Math.log10(j);
            int tempJ = j;
            M = j;
            for (int i = 0; i < logJ + 1; i++) {
                rest = tempJ % 10;
                tempJ = (int) (tempJ / 10);
                M += rest;
            }
            if (M == N) {
                answer = j;
                break;
            }
        }
        
        System.out.println(answer);
    }
}