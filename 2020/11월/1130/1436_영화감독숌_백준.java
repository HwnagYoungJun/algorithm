import java.util.*;


public class Main {
    static int N;
    static int count;
    static int maxValue;

    public static void main(String arg[]) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        count = 0;
        maxValue = 987654321;

        for (int i = 666; i < maxValue; i++) {
            String strI = Integer.toString(i);
            for (int j = 0; j < strI.length() - 2; j++) {
                if (strI.charAt(j) == '6') {
                    if (strI.charAt(j + 1) == '6' && (strI.charAt(j + 2) == '6')) {
                        count++;
                        break;
                    }
                }
            }
            if (count == N) {
                System.out.println(i);
                System.exit(0);
            }
        }
    }
}