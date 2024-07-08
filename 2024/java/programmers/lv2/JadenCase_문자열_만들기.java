package programmers.lv2;

import java.util.*;
public class JadenCase_문자열_만들기 {
    class Solution {
        public String solution(String s) {
            s = s.toLowerCase();
            StringTokenizer st = new StringTokenizer(s, " ", true);

            StringBuilder ans = new StringBuilder();

            while (st.hasMoreTokens()) {
                String word = st.nextToken();
                if(word.length() == 0)
                    ans.append(" ");
                else
                    ans.append(word.substring(0, 1).toUpperCase() + word.substring(1));
            }

            return ans.toString();

        }
    }
}
