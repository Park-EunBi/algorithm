package programmers.lv2;
import java.util.*;

public class 두_원_사이의_정수_쌍 {

    class Solution {
        public long solution(int r1, int r2) {
            long ans = 0;

            // x: i일 때 r1원 내부의 정수의 개수
            // cnt = Math.floor((Math.sqrt(Math.pow(r1, 2) - Math.pow(i, 2))))

            for (int i = 1; i <= r2; i++) {
                double mn = Math.sqrt(Math.pow(r1, 2) - Math.pow(i, 2));
                double mx = Math.sqrt(Math.pow(r2, 2) - Math.pow(i, 2));

                ans += (long)Math.floor(mx) - (long)Math.ceil(mn) + 1;
            }
            ans *= 4;

            return ans;
        }
    }
}
