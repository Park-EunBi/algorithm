#include <bits/stdc++.h>
using namespace std;

int n;
int m;
int board[505][505];
int visited[505][505];
int dxs[4] = {1, -1, 0, 0};
int dys[4] = {0, 0, 1, -1};
int mx;
int cnt;

int bfs(queue<pair<int,int>> q){
    int cnt = 1;
    while (q.size()){
        pair<int, int> cur = q.front(); q.pop();
        for (int dir = 0; dir < 4; dir ++) {
            int nx = cur.first + dxs[dir];
            int ny = cur.second + dys[dir];
            if (board[nx][ny] == 1 and visited[nx][ny] == 0) {
                q.push({nx, ny});
                visited[nx][ny] = 1;
                cnt += 1;
            }
        }
    }

    return cnt;
}

int main (){
    ios::sync_with_stdio(0);
    cin.tie(0);

    // input
    cin >> n >> m;

    for(int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> board[i][j];


    // main 
    for(int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
            if (board[i][j] and !visited[i][j]) {
                // queue 정의 
                queue<pair<int,int>> q;
                q.push({i, j});
                visited[i][j] = 1;
                mx = max(mx, bfs(q));
                cnt += 1;
            }
        }
    }
    

    // result
    cout << cnt << '\n';
    cout << mx;
}