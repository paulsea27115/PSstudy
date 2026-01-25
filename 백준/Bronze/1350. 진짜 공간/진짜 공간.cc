#include <iostream>

long long int li[51] = {0,};

int main()
{
    long long int t, store, res = 0;
    std::cin >> t;
    
    for(int i = 0; i < t; i++) {
        std::cin >> li[i];
    }
    
    std::cin >> store;
    
    for(int i = 0; i < t; i++){
        if(li[i]!=0) {
            if(li[i] % store != 0) res += 1;
            res += li[i] / store;
        }
    }
    
    std::cout << res * store;

    return 0;
}
