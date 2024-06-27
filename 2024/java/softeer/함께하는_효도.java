import java.io.*;
import java.util.*;

public class Main {

    static class Pos {
        int y;
        int x;

        public Pos(int y, int x) {
            this.y = y;
            this.x = x;
        }
    }

    public static void main(String[] args) throws Exception {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        String str = reader.readLine();
        String[] inputs = str.split(" ");
        int n = Integer.parseInt(inputs[0]);
        int m = Integer.parseInt(inputs[1]);
        int arr[][] = new int[n+1][n+1];
        for(int i=1; i<=n; i++) {
            String[] input = reader.readLine().split(" ");
            for(int j=1; j<=n; j++) {
                arr[i][j] = Integer.parseInt(input[j-1]);
            }
        }

        int[] answer = new int[1];

        int sum = 0;
        List<Pos> workerList = new ArrayList<Pos>();
        for(int i=0; i<m; i++) {
            String[] pos = reader.readLine().split(" ");
            int y = Integer.parseInt(pos[0]);
            int x = Integer.parseInt(pos[1]);
            workerList.add(new Pos(y, x));
            sum += arr[y][x];
            arr[y][x] = 0;
        }

        dfs(0, 0, workerList.get(0).y, workerList.get(0).x, m, sum, workerList, arr, answer);
        System.out.println(answer[0]);

    }

    static void dfs(int worker, int work, int y, int x, int m, int sum, List<Pos> workerList, int[][] arr, int[] answer) {


        answer[0] = Math.max(answer[0], sum);

        if (work == 3) {
            if(worker+1 < m)
                dfs(worker+1, 0, workerList.get(worker+1).y, workerList.get(worker+1).x, m, sum, workerList, arr, answer);
        } else {
            int[][] dir = {{-1,0}, {1,0}, {0,-1}, {0,1}};
            for(int i=0; i<4; i++) {
                int ny = y + dir[i][0];
                int nx = x + dir[i][1];

                if(ny>=1 && ny<arr.length && nx>=1 && nx<arr.length) {
                    int value = arr[ny][nx];
                    arr[ny][nx] = 0;
                    dfs(worker, work+1, ny, nx, m, sum+value, workerList, arr, answer);
                    arr[ny][nx] = value;
                }
            }
        }

    }

}