#include <bits/stdc++.h>
using namespace std;

int n, m;
string board[105]; // input: '1001100'
int visited[105][105];
int dxs[4] = {0, 0, 1, -1};
int dys[4] = {1, -1, 0, 0};
queue<pair<int, int>> q;

bool in_range(int x, int y) {
    if (x < 0 or x >= n or y < 0 or y >= m)
        return false;
    return true;
}

void bfs(){
    while (q.size()){
        auto cur  = q.front(); q.pop();
        for (int dir = 0; dir < 4; dir++) {
            int nx = cur.first + dxs[dir];
            int ny = cur.second + dys[dir];
            if (in_range(nx, ny) and board[nx][ny] == '1' and !visited[nx][ny]) {
                q.push({nx, ny});
                visited[nx][ny] = visited[cur.first][cur.second] + 1;
            }
        }
    }    
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    // input
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> board[i];

    // main 
    q.push({0, 0});
    visited[0][0] = 1;
    bfs();

    // result
    cout << visited[n-1][m-1];
}