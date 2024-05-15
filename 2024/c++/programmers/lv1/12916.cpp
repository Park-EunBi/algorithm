#include <string>
#include <iostream>
#include <stdio.h>
using namespace std;

bool solution(string s)
{
    int p = 0;
    int y = 0;
    bool ans = true;
    
    for (int i = 0; i < s.size(); i++)
        if (s[i] == 'P' or s[i] == 'p')
            p += 1;
        else if (s[i] == 'Y' or s[i] == 'y')
            y += 1;
            
    
    if (p != y)
        ans = false;
    
    return ans;
}