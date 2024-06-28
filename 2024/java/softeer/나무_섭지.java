import java.io.*;
import java.util.*;


public class Main {
    static int n, m; // 맵의 크기
    static char[][] board; // 맵 정보
    static int[][] namwooVisited; // 남우의 이동 경로 기록
    static int[][] ghostVisited; // 고스트의 이동 경로 기록
    static Queue<int[]> namwoo = new LinkedList<>(); // 남우의 BFS 큐
    static Queue<int[]> ghost = new LinkedList<>(); // 고스트의 BFS 큐
    static int[] dx = new int[]{-1, 0, 1, 0}; // 방향 배열 (상, 좌, 하, 우)
    static int[] dy = new int[]{0, -1, 0, 1}; // 방향 배열 (상, 좌, 하, 우)

    // 고스트의 BFS
    public static void ghostBfs() {
        while (!ghost.isEmpty()) {
            int[] ghostCoord = ghost.poll();
            int x = ghostCoord[0];
            int y = ghostCoord[1];

            for (int i = 0; i < 4; i++) {
                int gx = x + dx[i];
                int gy = y + dy[i];

                if (gx < 0 || gy < 0 || gx >= n || gy >= m) continue; // 범위를 벗어나면 무시
                if (ghostVisited[gx][gy] > 0) continue; // 이미 방문한 곳이면 무시
                ghost.offer(new int[]{gx, gy}); // 큐에 추가
                ghostVisited[gx][gy] = ghostVisited[x][y] + 1; // 이동 거리 기록
            }
        }
    }

    // 남우의 BFS
    public static boolean namwooBfs() {
        while (!namwoo.isEmpty()) {
            int[] namwooCoord = namwoo.poll();
            int x = namwooCoord[0];
            int y = namwooCoord[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (nx < 0 || ny < 0 || nx >= n || ny >= m) continue; // 범위를 벗어나면 무시
                if (board[nx][ny] == '#') continue; // 벽이면 무시
                if (namwooVisited[nx][ny] > 0) continue; // 이미 방문한 곳이면 무시
                if (namwooVisited[x][y] + 1 >= ghostVisited[nx][ny]) continue; // 고스트가 도착할 곳이면 무시
                namwoo.offer(new int[]{nx, ny}); // 큐에 추가
                namwooVisited[nx][ny] = namwooVisited[x][y] + 1; // 이동 거리 기록

                if (board[nx][ny] == 'D') return true; // 도착 지점에 도달하면 true 반환
            }
        }

        return false; // 탈출 실패
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        board = new char[n][m];
        ghostVisited = new int[n][m];
        namwooVisited = new int[n][m];

        for (int i = 0; i < n; i++) {
            char[] info = br.readLine().toCharArray();
            for (int j = 0; j < m; j++) {
                board[i][j] = info[j];
                if (board[i][j] == 'G') { // 고스트의 위치
                    ghost.offer(new int[]{i, j});
                    ghostVisited[i][j] = 1;
                } else if (board[i][j] == 'N') { // 남우의 위치
                    namwoo.offer(new int[]{i, j});
                    namwooVisited[i][j] = 1;
                }
            }
        }

        ghostBfs(); // 고스트의 BFS 실행

        boolean isEscape = namwooBfs(); // 남우의 BFS 실행

        if (isEscape) {
            System.out.println("Yes"); // 탈출 성공
        } else {
            System.out.println("No"); // 탈출 실패
        }
    }
}
"""
package softeer;

public class 나무_섭지 {
    static int n, m;
    static char[][] board;
    static Queue<int[]> namwoo = new LinkedList<>();
    static Queue<int[]> ghost = new LinkedList<>();
    static int[] dxs = new int[]{-1, 1, 0, 0};
    static int[] dys = new int[]{0, 0, 1, -1};
    static int[][] g_visited;
    static int[][] n_visited;

    public static void g_bfs() {
        while (!ghost.isEmpty()) {
            int[] loc = ghost.poll();
            int x = loc[0];
            int y = loc[1];
            for (int i = 0; i < 4; i++) {
                int nx = x + dxs[i];
                int ny = y + dys[i];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                if (g_visited[nx][ny] > 0) continue;
                ghost.offer(new int[]{nx, ny});
                g_visited[nx][ny] = g_visited[x][y] + 1;

                // if (g_visited[nx][ny] == 0) {
                // ghost.offer(new int[]{nx, ny});
                // g_visited[nx][ny] = g_visited[x][y] + 1;
                // }
            }
        }
    }

    public static boolean n_bfs() {
        while (!namwoo.isEmpty()) {
            int[] loc = namwoo.poll();
            int x = loc[0];
            int y = loc[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dxs[i];
                int ny = y + dys[i];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                if (board[nx][ny] == '#') continue;
                if (n_visited[nx][ny] > 0) continue;
                if (n_visited[x][y] + 1 >= g_visited[nx][ny]) continue;
                namwoo.offer(new int[]{nx, ny});
                n_visited[nx][ny] = n_visited[x][y] + 1;

                // if (n_visited[nx][ny] == 0 && board[nx][ny] == '.' && (g_visited[nx][ny] == 0 || n_visited[x][y] + 1 < g_visited[nx][ny])) {
                // namwoo.offer(new int[]{nx, ny});
                // n_visited[nx][ny] = n_visited[nx][ny] + 1;
                // }

                if (board[nx][ny] == 'D')
                    return true;
            }
        }
        return false;
    }


    public static void main(String[] args) throws IOException {
        // input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        board = new char[n][m];
        g_visited = new int[n][m];
        n_visited = new int[n][m];

        for (int i = 0; i < n; i++) {
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

        // bfs
        g_bfs();
        boolean isEscape = n_bfs();

        if (isEscape) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }

    }
}
"""