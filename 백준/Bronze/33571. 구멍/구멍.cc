#include <iostream>
#include <string>

using namespace std;

int main()
{
    string s, check("AabDdegOoPpQqR@"), d("B");
    getline(cin, s);
    
    int ans = 0;
    
    for(int i = 0; i < s.length(); i++) {
        if(check.find(s[i]) !=  string::npos) ans += 1;
        else if(d.find(s[i]) !=  string::npos) ans += 2;
    }
    
    cout << ans;
    
    return 0;
}