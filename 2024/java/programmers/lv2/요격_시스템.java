package programmers.lv2;

public class 요격_시스템 {
    import java.util.*;

    class Solution {
        public int solution(int[][] targets) {
            // 1. [0] 기준 정렬
            Arrays.sort(targets, (o1, o2) -> (o1[1] - o2[1]));

            // 2. 한 번에 요격할 수 있는지 판단
            int idx = 0;
            int cnt = 1; // 모두 한 번에 요격 가능하면 미사일의 최솟값은 1

            for (int i = 1 ; i < targets.length; i++){
                // 한 번에 요격 불가 (같은 x 상에 있지 않음)
                if (targets[idx][1] <= targets[i][0]) {
                    idx = i;
                    cnt += 1;
                }
            }
            return cnt;
        }
    }
}
