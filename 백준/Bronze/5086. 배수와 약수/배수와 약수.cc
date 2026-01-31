#include <iostream>
#include <string>

int main()
{
    std::string s;
    
    while(true){
        int a, b;
        
        std::cin >> a >> b;
        
        if(a == b) break;
        else if(a > b) s = (a % b == 0 ? "multiple" : "neither");
        else if(a < b) s = (b % a == 0 ? "factor" : "neither");
        
        std::cout << s << "\n";
    }

    return 0;
}