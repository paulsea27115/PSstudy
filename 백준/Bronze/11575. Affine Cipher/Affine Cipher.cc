#include <iostream>

using namespace std;

int main()
{
    int t;
    cin >> t;
    
    while(t--) {
        int a, b;
        cin >> a >> b;
        
        string s;
        cin >> s;
        
        string res("");
        for(const char &one_s: s) {
            res += (char)((((int)one_s - 65) * a + b) % 26 + 65);
        }
        
        cout << res << "\n";
    }

    return 0;
}