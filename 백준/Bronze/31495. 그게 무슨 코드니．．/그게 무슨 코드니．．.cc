#include <iostream>

int main()
{
    std::string s;
    
    std::getline(std::cin, s);
    
    if(s.length() > 2 && s[0] == '"' && s[s.length()-1] == '"') {
        std::cout << s.substr(1, s.length() - 2);
    } else {
        std::cout << "CE";
    }

    return 0;
}