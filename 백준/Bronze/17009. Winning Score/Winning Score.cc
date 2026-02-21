#include <iostream>

using namespace std;

int main()
{
    int a, res = 0, check = 3;
    const int half = 3;
    
    for(int i = 0; i < 6; i++) {
        cin >> a;
        res += (i < half? a: -a) * check;
        check -= half - 1 == i ? -2: 1;
    }
    
    cout << (res == 0 ? "T" : res < 0 ? "B" : "A");

    return 0;
}