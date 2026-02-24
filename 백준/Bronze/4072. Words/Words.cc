#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
    while(true) {
        string s;
        string ans("");
        
        getline(cin, s);
        
        if(s == "#") break;
        
        stack<char> st;
        
        for(int i = 0; i < s.length(); i++) {
            st.push(s[i]);
            if(s[i] == ' ') {
                st.pop();
                while(!st.empty()) {
                    ans += st.top();
                    st.pop();
                }
                ans += " ";
            }
        }
        
        while(!st.empty()) {
            ans += st.top();
            st.pop();
        }
        
        cout << ans << "\n";
    }

    return 0;
}