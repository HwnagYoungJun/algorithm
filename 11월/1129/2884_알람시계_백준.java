import java.util.*;


public class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        int H;
        int M;
        int wakeTime;

        H = sc.nextInt();
        M = sc.nextInt();

        wakeTime= H * 60 + M;

        if (wakeTime >= 45) {
            wakeTime -= 45;
        } else {
            wakeTime = (23 * 60) + (60 + M - 45);
        }
        H = (int)(wakeTime / 60);
        M = wakeTime % 60;

        System.out.printf("%d %d", H, M);
    }
}