
#include <iostream>

int main()
{
    int li[9][9] = {0,};
    int row = 0, column = 0, max = -1;
    
    for(int i = 1; i < 10; i++) {
        for(int j = 1; j < 10; j ++) {
            int a = 0;
            std::cin >> a;
            
            if(a > max) {
                column = i;
                row = j;
                
                max = a;
            }
        }
    }
    
    std::cout << max << std::endl << column << " " << row;
    
    return 0;
}