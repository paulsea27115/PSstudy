#include <iostream>

int main()
{
    int a, b, c;
    
    std::cin >> a >> b >> c;
    
    int res = 0;
    
    res = b / a;
    
    res *= 3;
    
    res *= c;
    
    std::cout << res;

    return 0;
}