#include <iostream>
#include <string>
using namespace std;

int main()
{
    string s, al("abcdefghijklmnopqrstuvwxyz");
    
    while(true) {
        getline(cin, s);
        if(s == "*") break;
        
        char ans = 'Y';
        
        for(short i = 0; i < 26; i++) {
            bool check = true;
            for(int j = 0; j < s.length(); j++) {
                if(s[j] == al[i]) {
                    check = false;
                    break;
                }
            }
            
            if(check) {
                ans = 'N';
                break;
            }
        }
        
        cout << ans << "\n";
        
    }

    return 0;
}