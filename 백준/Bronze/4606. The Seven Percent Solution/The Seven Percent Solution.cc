#include <iostream>
#include <string>

using namespace std;

string check(char n){
    string res;
    switch(n){
        case ' ':
            res = "%20";
            break;
        case '!':
            res = "%21";
            break;
        case '$':
            res = "%24";
            break;
        case '%':
            res = "%25";
            break;
        case '(':
            res = "%28";
            break;
        case ')':
            res = "%29";
            break;
        case '*':
            res = "\%2a";
            break;
        default:
            res += n;
    };
    
    return res;
}

int main()
{
    string s;
    while(true){
        getline(cin, s);
        if(s == "#") break;
        
        string res = "";
        for(int i = 0; i < s.length(); i++) {
            res += check(s[i]);
        }
        
        cout << res << "\n";
    }

    return 0;
}