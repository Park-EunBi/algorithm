#include <stdio.h>
using namespace std;

// dp[i][0]: fibo(i) 를 호출했을 때 0 출력 횟수
// dp[i][1]: fibo(i) 를 호출했을 때 1 출력 횟수
int dp[41][2];

int main(){

    // 초기화 
    dp[0][0] = 1;
    dp[1][1] = 1;

    // 점화식 
    for(int i = 2; i <41; i++){
        dp[i][0] = dp[i-1][0] + dp[i-2][0];
        dp[i][1] = dp[i-1][1] + dp[i-2][1];
    }

    int t;
    scanf("%d", &t);

    for(int i = 0; i < t; i++){
        int num;
        scanf("%d", &num);
        printf("%d %d\n", dp[num][0], dp[num][1]);
    }

    return 0;
}