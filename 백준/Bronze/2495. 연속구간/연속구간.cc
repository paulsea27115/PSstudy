#include <iostream>

int main(){
    int t = 3;
    
    for(int i = 0; i < t; i++) {
        std::string s;
        int max = 0, check = 0;
        
        std::cin >> s;
        char c = s[0]; 
        
        for(int j = 0; j < s.length(); j++) {
            check = c == s[j] ? check + 1 : 1;
            
            max = check > max ? check : max;
            
            c = s[j];
        }
        
        std::cout << max << "\n";
    }
    
    return 0;
}