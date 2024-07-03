package programmers.lv2;

public class 최댓값과_최솟값 {
    class Solution {
        public String solution(String s) {
            String nums[] = s.split(" ");
            int mx = Integer.parseInt(nums[0]);
            int mn = Integer.parseInt(nums[0]);

            for (String n: nums) {
                int num = (Integer.parseInt(n));
                mx = Math.max(mx, num);
                mn = Math.min(mn, num);
            }
            return mn + " " + mx;
        }
    }
}
