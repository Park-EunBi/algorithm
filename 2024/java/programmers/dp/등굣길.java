package programmers.dp;

public class 등굣길 {
    class Solution {
        public int solution(int m, int n, int[][] puddles) {
            // 0. board 채우기 (1: 웅덩이)
            int[][] board = new int[n][m];
            if (puddles[0].length > 0){
                for (int i = 0 ; i < puddles.length; i++) {
                    board[puddles[i][1] - 1][puddles[i][0] - 1] = 1;
                }
            }

            // 1. dp 정의
            int[][] dp = new int[n][m];

            // 2. 초기화
            // 2-1. 원점 - 출발 지점에는 웅덩이가 없음
            dp[0][0] = 1;

            // 2-2. (i, 0) - 위에서만 올 수 있음
            for (int i = 0 ; i < n; i++) {
                if (board[i][0] == 1) {
                    break;
                }
                dp[i][0] = 1;
            }


            // 2-2. (0, j) - 왼쪽에서만 올 수 있음
            for (int j = 0 ; j < m; j++){
                if(board[0][j] == 1) {
                    break;
                }
                dp[0][j] = 1;
            }


            // 3. 점화식
            for (int i = 1; i < n; i++) {
                for (int j = 1; j < m; j++) {
                    // 왼쪽, 위쪽에서 온 값 더하기
                    if (board[i][j] == 0) // 웅덩이라면 비워두기
                        dp[i][j] = (dp[i][j-1] + dp[i-1][j]) % 1000000007;
                }
            }

            // 4. output
            return dp[n-1][m-1] % 1000000007;
        }
    }
}
