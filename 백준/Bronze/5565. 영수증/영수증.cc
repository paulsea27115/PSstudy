#include <iostream>

using namespace std;

int main()
{
    int num = 0 ,res = 0;
    cin >> res;
    
    for(int i = 0; i < 9; i++){
        cin >> num;
        res -= num;
    }
    
    cout << res;

    return 0;
}