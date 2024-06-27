#include <iostream>

using namespace std;

int main()
{
    int day_count, pages;
    cin >> day_count >> pages;
    
    int result = 1, current_pages = pages;
    
    for(int i = 0; i < day_count; i++) {
        int number;
        cin >> number;
        
        if(number > current_pages) {
            result += 1;
            current_pages = pages;
        }
        current_pages -= number;
    }
    
    cout << result;

    return 0;
}