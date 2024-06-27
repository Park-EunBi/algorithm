import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String s = st.nextToken();
            String t = st.nextToken();
            s = s.toUpperCase();

            int idx = s.indexOf('X');
            sb.append(t.substring(idx, idx+1).toUpperCase());
        }

        String ans = sb.toString();
        System.out.println(ans);

    }
}
