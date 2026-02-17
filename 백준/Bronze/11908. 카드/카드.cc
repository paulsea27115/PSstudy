#include <iostream>

using namespace std;

int main()
{
    int t, max = 0, res = 0;
    cin >> t;
    
    for(int i = 0; i < t; i++) {
        int a;
        cin >> a;
        
        res += a;
        
        if(max < a) max = a;
    }
    
    cout << res - max;
    
    return 0;
}