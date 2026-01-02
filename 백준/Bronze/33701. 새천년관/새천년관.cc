#include <iostream>

int main()
{
    std::string s("nowpaulseatechuniversityofkoreagwan");
    
    for(int i = 0; i < s.length(); i++) {
        char word = s[i] - 1;
        
        std::cout << char(word + 1);
    }

    return 0;
}