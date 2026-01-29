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
    std::reverse(check_s.begin(), check_s.end());
    
    for(int i = 0; i < s.length(); i++){
        dq.push_back(s[i]);
        
        if(check_s.length() <= dq.size()) {
            std::deque<char> _dq;
            for(int j = 0; j < check_s.length(); j++) {
                _dq.push_back(dq.back());
                dq.pop_back();
            }
            
            if(std::string(_dq.begin(), _dq.end()) == check_s) {
                continue;
            } else {
                for(int j = 0; j < check_s.length(); j++) {
                    dq.push_back(_dq.back());
                    _dq.pop_back();
                }
            }
        }
    }
    
    std::string ans(dq.begin(), dq.end());
    
    std::cout << ans;
    return 0;
}