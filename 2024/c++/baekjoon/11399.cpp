#include <stdio.h>
#include <algorithm>
using namespace std;

int arr[1001];
int dp[1001];

int main() {
    int n;
    int ans = 0;

    scanf("%d", &n);

    for(int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    sort(arr, arr+n);

    dp[0] = arr[0];
    for(int i = 1; i < n; i++) {
        dp[i] = dp[i-1] + arr[i];
    }

    for(int i = 0; i < n; i++)
        ans += dp[i];

    printf("%d", ans);
    return 0;
}