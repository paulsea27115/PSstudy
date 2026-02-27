#include <iostream>
#include <string>
#include <map>
#include <cmath>

using namespace std;

int main()
{
    int a, b;
    
    cin >> a >> b;
    
    cout << (b - (a >= 20 ? - (24 - a) : a));

    return 0;
}