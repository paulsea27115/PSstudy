#include <iostream>

int main(){
    int a = 0;
    std::string str;
    
    while(true){
        std::cin >> str;
        
        if("animal" == str){
            std::cout << "Panthera tigris" << std::endl;
        } else if ("tree" == str) {
            std::cout << "Pinus densiflora" << std::endl;
        } else if("flower" == str){
            std::cout << "Forsythia koreana" << std::endl;
        } else {
            break;
        }
    }
    
    return 0;
}