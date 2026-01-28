#include <bits/stdc++.h>

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t;
    
    std::vector<std::pair<int, int>> v; 
    
    for(int i = 0; i < t; i++) {
        int a, b;
        std::cin >> a >> b;
        
        v.emplace_back(std::make_pair(a,1));
        v.emplace_back(std::make_pair(b,-1));
    }
    
    sort(v.begin(), v.end());
    
    int cur = 0;
    int cnt = 0;
    
    for(int i = 0; i < v.size() - 1; i++) {
        cur += v[i].second;
        
        if(cur > 0) {
            cnt += v[i + 1].first - v[i].first;
        }
    }
    
    std::cout << cnt;
}