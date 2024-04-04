#include <iostream>
#include <string>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    string s;
    cin >> s;
    int ans = 0;
    for (int i=0;i<m;i++) {
        int k=0; 
        if(s[i]=='O') continue;
        else {
            while(i+1<m&&s[i+1]=='O'&&i+2<m&&s[i+2]=='I'){
                k++;
                if(k==n){k--;ans++;}
                i+=2; 
            } k = 0;
        }
    }
    cout << ans << endl;
    return 0;
}
