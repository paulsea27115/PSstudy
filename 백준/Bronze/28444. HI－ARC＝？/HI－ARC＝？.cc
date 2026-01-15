#include <iostream>

int main()
{
    int h,i,a,r,c;
    
    std::cin >> h >> i >> a >> r >> c;
    
    int res = 0;
    
    res = h * i - a * r * c;
    
    std::cout << res;

    return 0;
}