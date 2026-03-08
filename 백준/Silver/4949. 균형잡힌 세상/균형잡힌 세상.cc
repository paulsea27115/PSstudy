#include <bits/stdc++.h>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    
    string s;
    while(true){
        getline(cin, s);
        
        if(s == ".") break;
        stack<char> a;
        bool check = false;
        
        for(int i = 0; i < s.length(); i++) {
            if(s[i] == '(') a.push(')');
            else if(s[i] == '[') a.push(']');
            else if(s[i] == ')' || s[i] == ']') {
                if(a.empty() || s[i] != a.top()) check = true;
                else a.pop();
            }
        }
        
        if(!a.empty()) check = true;
        
        cout << (check ? "no" : "yes") << "\n";
    }

    return 0;
}