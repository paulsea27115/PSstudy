#include <iostream>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    while(true){
        int a, res = 0;
        cin >> a;
        
        if(a == 0) break;
        
        for(int i = 1; i <= a; i++) {
            for(int j = 1; j <= a; j++) {
                res += i *j;
            }
        }
        
        cout << res << "\n";
    }

    return 0;
}