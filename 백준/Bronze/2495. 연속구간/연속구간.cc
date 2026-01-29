#include <bits/stdc++.h>

int main()
{
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int t = 3;
    
    for(int i = 0; i < t; i++) {
        std::string s;
        int max = 0, check = 0;
        
        std::cin >> s;
        char c = s[0]; 
        
        for(int j = 0; j < s.length(); j++) {
            check = c == s[j] ? check + 1 : 1;
            // std::cout << c << " " << s[j] << "\n";
            
            max = check > max ? check : max;
            
            c = s[j];
        }
        
        std::cout << max << "\n";
    }
    
    return 0;
    
}