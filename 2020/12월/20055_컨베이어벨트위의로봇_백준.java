import java.util.*;
import java.io.*;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int N;
        int K;
        int[] array;
        int step;
        int countOfZero;
        boolean[] robotArray;
        Queue<Integer> robotQueue;

        N = sc.nextInt();
        K = sc.nextInt();
        array = new int[2 * N];
        sc.nextLine();
        String[] temp = sc.nextLine().split(" ");

        step = 0;
        countOfZero = 0;
        for (int i = 0; i < 2 * N; i++) {
            array[i] = Integer.parseInt(temp[i]);
        }

        robotArray = new boolean[2 * N];
        robotQueue = new LinkedList<>();

        while (countOfZero < K) {
            step++;

            // 1. 회전한다.
            int lastPoint = array[2 * N - 1];
            for (int i = 2 * N - 2; i > -1; i--) {
                array[i + 1] = array[i];
                if (robotArray[i]) {
                    if (i == N - 2){
                        robotArray[i] = false;
                        robotQueue.poll();
                        continue;
                    }
                    robotArray[i + 1] = true;
                    robotArray[i] = false;
                    robotQueue.poll();
                    robotQueue.offer(i + 1);
                }
            }
            array[0] = lastPoint;

            // 2. 로봇의 이동
            int queueSize = robotQueue.size();
            for (int i = 0; i < queueSize; i++){
                int pos = robotQueue.poll();
                if (pos == N - 2) {
                    if (array[pos + 1] != 0) {
                        robotArray[pos] = false;
                        array[pos + 1]--;
                        if (array[pos + 1] == 0) {
                            countOfZero++;
                        }
                    } else {
                        robotQueue.offer(pos);
                    }
                    continue;
                }
                if (array[pos + 1] != 0 && !robotArray[pos + 1]) {
                    robotQueue.offer(pos + 1);
                    robotArray[pos] = false;
                    robotArray[pos + 1] = true;
                    array[pos + 1]--;
                    if (array[pos + 1] == 0) {
                        countOfZero++;
                    }
                } else {
                    robotQueue.offer(pos);
                }
            }

            // 3. 로봇을 하나 올린다
            if (!robotArray[0] && array[0] != 0) {
                array[0]--;
                robotQueue.offer(0);
                robotArray[0] = true;
                if (array[0] == 0) {
                    countOfZero++;
                }
            }
        }

        System.out.print(step);
    }
}