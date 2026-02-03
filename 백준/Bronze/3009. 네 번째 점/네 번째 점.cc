#include <bits/stdc++.h>

int main() {
    std::unordered_map<int, int> m_l;
    std::unordered_map<int, int> m_r;
    
    for(int i = 0; i < 3; i++) {
        int a, b;
        std::cin >> a >> b;
        
        m_l[a]++;
        m_r[b]++;
    }
    
    std::vector<std::pair<int, int>> v_l(m_l.begin(), m_l.end());
    std::vector<std::pair<int, int>> v_r(m_r.begin(), m_r.end());
    
    int a, b;
    
    for(int i = 0; i < 3; i++) {
        if(v_l[i].second == 1) {
            a = v_l[i].first;
        }
        if(v_r[i].second == 1) {
            b = v_r[i].first;
        }
    }
    
    std::cout << a << " " << b;
    
    return 0;
}