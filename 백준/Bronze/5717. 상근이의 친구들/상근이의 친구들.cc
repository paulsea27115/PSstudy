#include <iostream>

int main()
{
    int a = 0, b = 0;
    
    while(true) {
        std::cin >> a >> b;
        
        if(a + b == 0) {
            break;
        }
        
        std::cout << a + b << "\n";
    }

    return 0;
}