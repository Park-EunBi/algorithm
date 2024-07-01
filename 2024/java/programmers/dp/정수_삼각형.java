package programmers.dp;

public class 정수_삼각형 {
    class Solution {
        public int solution(int[][] triangle) {
            int n = triangle.length;
            int m = triangle[n-1].length;

            // 1. dp 정의 - (i, j) 위치까지의 경로 중 숫자의 합의 최댓값
            int[][] dp = new int[n][m];

            // 2. dp 초기화
            // 2-1. dp[0][0] 초기화
            dp[0][0] = triangle[0][0];

            for (int i = 1 ; i < n; i++) {
                // 2-2. dp[i][0] 초기화
                dp[i][0] = dp[i-1][0] + triangle[i][0];

                //2-3. dp[i][cnt] 초기화
                dp[i][i] = dp[i-1][i-1] + triangle[i][i];
            }

            // 3. 점화식
            for (int i = 2; i < n; i++) {
                for (int j = 1; j < i; j++) {
                    dp[i][j] = Math.max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j];
                }
            }

            // 4. output
            int mx = 0;
            for (int j = 0; j < m; j++)
                mx = Math.max(mx, dp[n-1][j]);
            return mx;
        }
    }
}
