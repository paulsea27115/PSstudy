#include <iostream>

using namespace std;

int li[9] = {100, 100, 200, 200, 300, 300, 400, 400, 500};

int main()
{
    int n = 0;
    
    for(int i = 0; i < 9; i++) {
        int a;
        cin >> a;
        
        if(li[i] < a) {
            n = -1;
            break;
        }
        
        n += a;
    }
    
    if(n == -1) cout << "hacker";
    else if(n >= 100) cout << "draw";
    else cout << "none";
    
    return 0;
}