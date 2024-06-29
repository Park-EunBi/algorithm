import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[] nums;
    static int bigger;
    static long ans;

    public static void main(String[] args) throws IOException{
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());

        nums = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i = 0 ; i < n; i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }

        // 누적합
        for(int i = 0 ; i < n; i++) {
            bigger = 0;
            for (int k = i + 1; k < n; k++) {
                if (nums[i] < nums[k]) // 조건에 안맞음, a[i] 보다 큰 수라는 것만 체크
                    bigger += 1;
                else // 조건에 맞음 - 기존에 세었던 a[i] 보다 큰 값들 더해주기
                    ans += bigger;
            }
        }

        // output
        System.out.println(ans);
    }
}
