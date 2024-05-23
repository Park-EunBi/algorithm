#include <string>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

string solution(vector<string> cards1, vector<string> cards2, vector<string> goal) {
    
    int p1 = 0;
    int p2 = 0; 
    int cnt = 0;
    
    while (cnt < goal.size()) {
        if (cards1[p1] == goal[cnt]) {
            cnt += 1;
            p1 += 1;
        }
        else if (cards2[p2] == goal[cnt]) {
            cnt += 1;
            p2 += 1;
        }
        else {
            return "No";
        }
    }
    
    
    return "Yes";
}