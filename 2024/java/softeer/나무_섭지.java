import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static char[][] board;
    static Queue<int[]> ghost = new LinkedList<>();
    static Queue<int[]> namwoo = new LinkedList<>();
    static int[][] g_visited;
    static int[][] n_visited;
    static int[] dxs = {0, 0, 1, -1};
    static int[] dys = {-1, 1, 0, 0};

    public static boolean in_range(int x, int y) {
        if (x < 0 || x >= n || y < 0 || y >= m) return false;
        else return true;
    }

    public static void g_bfs(){
        while(!ghost.isEmpty()) {
            int[] info = ghost.poll();
            int x = info[0];
            int y = info[1];
            for (int i = 0 ; i < 4; i++) {
                int nx = x + dxs[i];
                int ny = y + dys[i];

                if (in_range(nx, ny) && g_visited[nx][ny] == 0){
                    ghost.offer(new int[]{nx, ny});
                    g_visited[nx][ny] = g_visited[x][y] + 1;
                }
            }
        }
    }

    public static boolean n_bfs(){
        while (!namwoo.isEmpty()) {
            int[] info = namwoo.poll();
            int x = info[0];
            int y = info[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dxs[i];
                int ny = y + dys[i];
                if (in_range(nx, ny) && (n_visited[nx][ny] == 0) && (board[nx][ny] == '.') && (g_visited[nx][ny] > n_visited[x][y] + 1)) {
                    namwoo.offer(new int[]{nx, ny});
                    n_visited[nx][ny] = n_visited[x][y] + 1;
                }
                if (in_range(nx,ny) && board[nx][ny] == 'D') return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new char[n][m];
        g_visited = new int[n][m];
        n_visited = new int[n][m];

        for (int i = 0 ; i < n; i++) {
            char[] info = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                board[i][j] = info[j];
                if (board[i][j] == 'G') {
                    ghost.offer(new int[]{i, j});
                    g_visited[i][j] = 1;
                } else if (board[i][j] == 'N') {
                    namwoo.offer(new int[]{i, j});
                    n_visited[i][j] = 1;
                }
            }
        }

        g_bfs();
        boolean ans = n_bfs();
        if (ans) System.out.println("Yes");
        else System.out.println("No");
    }
}
