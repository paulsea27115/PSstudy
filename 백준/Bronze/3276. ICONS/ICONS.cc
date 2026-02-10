#include <iostream>

using namespace std;

int main()
{
    int a;
    cin >> a;
    
    int i = 1, x = 1, y = 1;
    int j = 0;
    while(true) {
        if(i >= a) break;
        if(j % 2 == 0) y += 1;
        else x += 1;
        
        i += x;
        j += 1;
    }
    
    cout << x << " " << y;


    return 0;
}