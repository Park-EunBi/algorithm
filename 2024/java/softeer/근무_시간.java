package softeer;
import java.io.*;
import java.util.*;
public class 근무_시간 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ret = 0;
        for (int i = 0; i < 5; i++){
            String start = sc.next();
            String end = sc.next();
            int startH = Integer.parseInt(start.substring(0, 2));
            int startM = Integer.parseInt(start.substring(3, 5));
            int endH = Integer.parseInt(end.substring(0, 2));
            int endM = Integer.parseInt(end.substring(3, 5));
            ret += (60 - startM) + (endH - startH - 1) * 60 + endM;
        }
        System.out.println(ret);
        sc.close();
    }
}
