package softeer;
import java.io.*;
import java.util.*;
public class ab {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            System.out.println("Case #" + (i + 1) + ": " + (a + b));
        }
        sc.close();
    }
}

/**
 * import java.io.*;
 * import java.util.*;
 *
 * public class Main {
 *     public static void main(String[] args) throws Exception {
 *         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
 *         int T = Integer.parseInt(br.readLine());
 *         for(int t=1; t<=T; t++) {
 *             StringTokenizer st = new StringTokenizer(br.readLine());
 *             int a = Integer.parseInt(st.nextToken());
 *             int b = Integer.parseInt(st.nextToken());
 *             int res = a + b;
 *             System.out.println("Case #"+t+": " +res);
 *         }
 *     }
 * }
 */