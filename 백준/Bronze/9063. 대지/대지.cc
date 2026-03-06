#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    vector<int> vx;
    vector<int> vy;
    
    for(int i = 0; i < t; i++) {
        int x, y;
        cin >> x >> y;
        
        vx.emplace_back(x);
        vy.emplace_back(y);
    }
    
    sort(vx.begin(), vx.end());
    sort(vy.begin(), vy.end());
    
    cout << (vx.front() - vx.back()) * (vy.front() - vy.back());

    return 0;
}