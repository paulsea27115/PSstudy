#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    int n;
    cin >> n;
    
    int res = 0;
    for(int i = 1; i <= int(sqrt(n)); i++) {
        res += n / i - i + 1;
    }
    
    cout << res;
    return 0;
}