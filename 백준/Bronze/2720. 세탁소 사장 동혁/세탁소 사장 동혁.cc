#include <iostream>

int main()
{
    int t, a;
    
    int check[4] = {25,10,5,1};
    
    std::cin >> t;
    
    for(int i = 0; i < t; i++) {
        int res[4] = {0,};
        std::cin >> a;
        
        for(int j = 0; j < 4; j++) {
            res[j] = a / check[j];
            
            a %= check[j];
        }
        
        for(int j = 0; j < 4; j++) {
            std::cout << res[j] << " ";
        }
        
        std::cout << std::endl;
    }

    return 0;
}