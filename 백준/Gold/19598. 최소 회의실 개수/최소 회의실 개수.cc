#include <bits/stdc++.h>
#define ll long long int

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);

    int t;
    std::cin >> t;
    
    std::unordered_map<ll,ll> diff;
    
    for(int i = 0; i < t; i++) {
        ll a, b;
        std::cin >> a >> b;
        
        diff[a]++;
        diff[b]--;
    }
    
    std::vector<std::pair<ll, ll>> v(diff.begin(),diff.end());
    sort(v.begin(), v.end());
    
    int cur = 0;
    int max = 0;
    
    for(int i = 0; i < v.size() - 1; i++) {
        cur += v[i].second;
        
        max = max < cur ? cur: max;
    }
    
    std::cout << max;
}