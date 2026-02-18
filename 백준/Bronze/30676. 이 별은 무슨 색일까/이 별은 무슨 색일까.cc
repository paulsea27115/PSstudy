#include <iostream>
#include <string>

using namespace std;

int main()
{
    int li[7] = {620, 590, 570, 495, 450, 425, 380};
    string s[7] = {"Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"}; 

    int n, a = 0;
    cin >> n;
    
    for(; a < 8; a++) {
        if(li[a] <= n) {
            cout << s[a];
            break;
        }
    }
    
    return 0;
}