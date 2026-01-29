#include <iostream>
#include <string>
#include <deque>
#include <algorithm>

#define ll long long int

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    std::string s, check_s;
    
    std::deque<char> dq;
    
    std::cin >> s >> check_s;
    // std::reverse(check_s.begin(), check_s.end());
    
    for(int i = 0; i < s.length(); i++){
        dq.push_back(s[i]);
        
        if(check_s.length() <= dq.size()) {
            bool c = true;
            
            for(int j = 0; j < check_s.length(); j++) {
                if(check_s[j] != dq[dq.size() - (check_s.length() - j)]) {
                    c = false;
                    break;
                }
            }
            
            if(c) {
                for(int j = 0; j < check_s.length(); j++) {
                    dq.pop_back();
                }
            }
        }
    }
    
    std::string ans(dq.begin(), dq.end());
    
    std::cout << ans;
    return 0;
}