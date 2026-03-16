#include <iostream>

using namespace std;

int main()

{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t, res = 0, past = -1; 
    cin >> t;
    
    
    while(t--) {
        int a; cin >> a;
        
        if(a >= past) res += 1;
        past = a;
    }
    
    cout << res;
    
    return 0;
}