#include <bits/stdc++.h>
using namespace std;

int nums[100001];
bool calc[2000001];
int cnt;

int main(void){
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, x;
    cin >> n;

    for (int i = 0; i < n; i++)
        cin >> nums[i];
    cin >> x;

    for (int i = 0; i < n; i++) {
        // 짝이 양수이고, 짝이 nums에 존재하면
        if (x - nums[i] > 0 and calc[x-nums[i]])
            cnt += 1;
        // nums[i]가 등장했음을 표시
        calc[nums[i]] = true;
    }

    cout << cnt;
}