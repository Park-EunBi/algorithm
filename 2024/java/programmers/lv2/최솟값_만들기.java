package programmers.lv2;
import java.util.*;

public class 최솟값_만들기 {

    class Solution
    {
        public int solution(int []A, int []B)
        {
            int ans = 0;

            Arrays.sort(A);
            // Arrays.sort(B,Collections.reverseOrder()); // Integer 배열로 변환 필요
            Arrays.sort(B);

            for (int i = 0 ; i < A.length; i++)
                ans += (A[i] * B[B.length - i - 1]);

            return ans;
        }
    }
}
