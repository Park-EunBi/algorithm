import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] board;
    static int[][] time;
    static int[][] dp;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        board = new int[2][n + 1];
        time = new int[2][n + 1];
        dp = new int[2][n + 1];


        for(int i = 0; i < n-1; i++) {
            st = new StringTokenizer(br.readLine());
            board[0][i] = Integer.parseInt(st.nextToken());
            board[1][i] = Integer.parseInt(st.nextToken());
            time[0][i] = Integer.parseInt(st.nextToken());
            time[1][i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        board[0][n-1] = Integer.parseInt(st.nextToken());
        board[1][n-1] = Integer.parseInt(st.nextToken());

        // dp 초기화
        dp = new int[2][n+1];
        dp[0][0] = board[0][0];
        dp[1][0] = board[1][0];

        // 점화식
        // 현재 위치에 오기까지 이전 위치 이동 시간의 최솟값 파악
        for (int i = 1; i < n; i++) {
            dp[0][i] = Math.min(dp[0][i - 1], dp[1][i - 1] + time[1][i - 1]) + board[0][i];
            dp[1][i] = Math.min(dp[1][i - 1], dp[0][i - 1] + time[0][i - 1]) + board[1][i];
        }

        System.out.println(Math.min(dp[0][n-1], dp[1][n-1]));
    }

}
